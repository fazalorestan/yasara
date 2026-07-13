from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BUILD_ID = "2026.52.P.001"
LEGACY_ACCEPTED_BUILD_IDS = [
    "2026.52.K.001",
    "2026.52.L.001",
    "2026.52.M.001",
    "2026.52.N.001",
    "2026.52.O.001",
    "2026.52.P.001",
]

ROOT = Path(__file__).resolve().parents[1]
EXE = ROOT / "dist/windows/portable/YaSara/YaSara.exe"
REPORT_DIR = ROOT / "dist/windows/reports"
ARTIFACT_DIR = ROOT / "dist/windows/artifacts"
RUNTIME_REPORT = ROOT / "dist/windows/portable/YaSara/runtime_reports/launcher_report.json"
BACKEND_STDERR = ROOT / "dist/windows/portable/YaSara/runtime_reports/backend_stderr.log"
STAGE_ROOT = ROOT / ".build_stage"
STAGE_BACKEND = STAGE_ROOT / "backend"
PACKAGED_BACKEND = ROOT / "dist/windows/portable/YaSara/_internal/backend"

HEALTH_CANDIDATES = [
    "http://127.0.0.1:8000/api/v1/health",
    "http://127.0.0.1:8000/health",
    "http://127.0.0.1:8000/docs",
    "http://127.0.0.1:8000/openapi.json",
]

PACKAGE_MAP = {
    "fastapi": "fastapi",
    "starlette": "starlette",
    "pydantic": "pydantic",
    "pydantic_settings": "pydantic_settings",
    "uvicorn": "uvicorn",
    "anyio": "anyio",
    "httpx": "httpx",
    "sqlalchemy": "sqlalchemy",
    "cryptography": "cryptography",
    "ccxt": "ccxt",
    "numpy": "numpy",
    "pandas": "pandas",
    "orjson": "orjson",
    "certifi": "certifi",
    "dns": "dns",
    "websockets": "websockets",
    "typing_extensions": "typing_extensions",
    "dotenv": "dotenv",
    "yaml": "yaml",
    "PIL": "PIL",
    "aiosqlite": "aiosqlite",
    "apscheduler": "apscheduler",
}

ALWAYS_VALIDATE = {
    "fastapi",
    "starlette",
    "pydantic",
    "pydantic_settings",
    "uvicorn",
    "anyio",
    "sqlalchemy",
    "apscheduler",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def discover_import_roots() -> set[str]:
    roots: set[str] = set()
    for folder in [ROOT / "backend", ROOT / "desktop"]:
        if not folder.exists():
            continue
        for file in folder.rglob("*.py"):
            try:
                tree = ast.parse(file.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        roots.add(alias.name.split(".")[0])
                elif isinstance(node, ast.ImportFrom) and node.module:
                    roots.add(node.module.split(".")[0])
    return roots


def validate_dependencies() -> dict:
    discovered = discover_import_roots()
    packages = sorted(
        {PACKAGE_MAP[item] for item in discovered if item in PACKAGE_MAP}
        | ALWAYS_VALIDATE
    )
    missing: list[dict] = []
    checked: list[str] = []

    for package in packages:
        try:
            if importlib.util.find_spec(package) is None:
                raise ModuleNotFoundError(f"No module named '{package}'")
            checked.append(package)
        except Exception as exc:
            missing.append(
                {"package": package, "import": package, "error": str(exc)}
            )

    return {
        "ready": not missing,
        "checked": checked,
        "missing": missing,
        "discovered_import_roots": sorted(discovered),
        "validated_packages": packages,
    }


def validate_source_tree() -> dict:
    router = ROOT / "backend/app/api/v1/router.py"
    desktop = ROOT / "desktop/yasara_desktop.py"
    frontend_dist = ROOT / "frontend/dist/index.html"

    checks = {
        "router_exists": router.exists(),
        "desktop_entry_exists": desktop.exists(),
        "frontend_dist_exists": frontend_dist.exists(),
        "router_registry_only": False,
    }

    if router.exists():
        text = router.read_text(encoding="utf-8", errors="replace")
        checks["router_registry_only"] = (
            "runtime_auto_router_registry.register_all" in text
            and "from app.api.v1.routes import" not in text
            and "v418_launcher_v1" not in text
            and "include_router(v418_launcher_v1.router)" not in text
        )

    return {"ready": all(checks.values()), "checks": checks}


def _ignore_stage(path: str, names: list[str]) -> set[str]:
    ignored = {"__pycache__", ".pytest_cache", ".mypy_cache"}
    ignored.update(name for name in names if name.endswith((".pyc", ".pyo")))
    if Path(path).name == "backend":
        ignored.add("tests")
    return ignored


def prepare_clean_stage() -> dict:
    source = ROOT / "backend"
    if not source.exists():
        return {"ready": False, "reason": "backend_source_missing"}

    shutil.rmtree(STAGE_ROOT, ignore_errors=True)
    STAGE_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, STAGE_BACKEND, ignore=_ignore_stage)

    source_router = source / "app/api/v1/router.py"
    staged_router = STAGE_BACKEND / "app/api/v1/router.py"

    result = {
        "ready": staged_router.exists(),
        "source_router": str(source_router),
        "staged_router": str(staged_router),
    }

    if source_router.exists() and staged_router.exists():
        result["source_sha256"] = sha256(source_router)
        result["staged_sha256"] = sha256(staged_router)
        result["ready"] = result["source_sha256"] == result["staged_sha256"]

    return result


def clean_previous_outputs() -> None:
    shutil.rmtree(ROOT / "build/windows/YaSara", ignore_errors=True)
    shutil.rmtree(ROOT / "dist/windows/portable/YaSara", ignore_errors=True)


def run_build() -> int:
    env = os.environ.copy()
    env["YASARA_BUILD_STAGE"] = str(STAGE_ROOT)
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        "--distpath",
        str(ROOT / "dist/windows/portable"),
        "--workpath",
        str(ROOT / "build/windows"),
        str(ROOT / "packaging/windows/YaSara.spec"),
    ]
    return subprocess.run(cmd, cwd=str(ROOT), env=env, shell=False).returncode


def validate_packaged_backend() -> dict:
    source_router = ROOT / "backend/app/api/v1/router.py"
    staged_router = STAGE_BACKEND / "app/api/v1/router.py"
    packaged_router = PACKAGED_BACKEND / "app/api/v1/router.py"

    checks = {
        "source_exists": source_router.exists(),
        "stage_exists": staged_router.exists(),
        "packaged_exists": packaged_router.exists(),
        "hash_match": False,
        "packaged_router_clean": False,
    }

    hashes = {}
    for key, path in [
        ("source", source_router),
        ("stage", staged_router),
        ("packaged", packaged_router),
    ]:
        if path.exists():
            hashes[key] = sha256(path)

    if len(hashes) == 3:
        checks["hash_match"] = len(set(hashes.values())) == 1

    if packaged_router.exists():
        text = packaged_router.read_text(encoding="utf-8", errors="replace")
        checks["packaged_router_clean"] = (
            "from app.api.v1.routes import" not in text
            and "v418_launcher_v1" not in text
            and "runtime_auto_router_registry.register_all" in text
        )

    return {"ready": all(checks.values()), "checks": checks, "hashes": hashes}


def probe(url: str) -> tuple[bool, int | str]:
    try:
        with urllib.request.urlopen(url, timeout=2) as response:
            return 200 <= response.status < 500, response.status
    except Exception as exc:
        return False, str(exc)


def wait_health(seconds: int = 60) -> tuple[bool, str | None, int | str | None, dict]:
    end = time.time() + seconds
    results: dict[str, int | str] = {}

    while time.time() < end:
        for url in HEALTH_CANDIDATES:
            ok, status = probe(url)
            results[url] = status
            if ok:
                return True, url, status, results
        time.sleep(0.5)

    return False, None, None, results


def terminate_process(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=10)


def validate_executable() -> dict:
    if not EXE.exists():
        return {"ready": False, "reason": "exe_missing"}

    if RUNTIME_REPORT.exists():
        RUNTIME_REPORT.unlink()

    proc = subprocess.Popen([str(EXE)], cwd=str(EXE.parent))
    health_ok = False
    health_url = None
    health_status = None
    probe_results = {}

    try:
        health_ok, health_url, health_status, probe_results = wait_health(60)
    finally:
        terminate_process(proc)

    runtime = None
    if RUNTIME_REPORT.exists():
        try:
            runtime = json.loads(RUNTIME_REPORT.read_text(encoding="utf-8"))
            health_ok = bool(runtime.get("backend_health_ok")) or health_ok
            health_url = runtime.get("backend_health_url") or health_url
            health_status = runtime.get("backend_health_status") or health_status
            probe_results = runtime.get("probe_results") or probe_results
        except Exception:
            pass

    stderr = (
        BACKEND_STDERR.read_text(encoding="utf-8", errors="replace")
        if BACKEND_STDERR.exists()
        else ""
    )

    return {
        "ready": health_ok,
        "exe_return_code": proc.returncode,
        "health_ok": health_ok,
        "health_url": health_url,
        "health_status": health_status,
        "probe_results": probe_results,
        "runtime_report": runtime,
        "backend_stderr_tail": stderr[-8000:],
    }


def write_report(report: dict) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "build_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--skip-exe-validation", action="store_true")
    args = parser.parse_args()

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    dependency = validate_dependencies()
    source_validation = validate_source_tree()

    report = {
        "build_id": BUILD_ID,
        "legacy_accepted_build_ids": LEGACY_ACCEPTED_BUILD_IDS,
        "dependency_validation": dependency,
        "source_validation": source_validation,
    }

    if not dependency["ready"]:
        report.update(
            {
                "return_code": 10,
                "exe_exists": EXE.exists(),
                "executable_validation": {
                    "ready": False,
                    "reason": "dependency_validation_failed",
                },
            }
        )
        write_report(report)
        print(json.dumps(report, indent=2))
        return 10

    if not source_validation["ready"]:
        report.update(
            {
                "return_code": 11,
                "exe_exists": EXE.exists(),
                "executable_validation": {
                    "ready": False,
                    "reason": "source_validation_failed",
                },
            }
        )
        write_report(report)
        print(json.dumps(report, indent=2))
        return 11

    stage = prepare_clean_stage()
    report["staging"] = stage
    if not stage.get("ready"):
        report["return_code"] = 12
        write_report(report)
        print(json.dumps(report, indent=2))
        return 12

    if not args.execute:
        report.update({"dry_run": True, "return_code": 0})
        write_report(report)
        print(json.dumps(report, indent=2))
        return 0

    clean_previous_outputs()
    rc = run_build()

    report["return_code"] = rc
    report["exe_exists"] = EXE.exists()
    report["exe_path"] = str(EXE)

    if EXE.exists():
        digest = sha256(EXE)
        (ARTIFACT_DIR / "YaSara.exe.sha256").write_text(digest, encoding="utf-8")
        report["sha256"] = digest

    packaged = validate_packaged_backend()
    report["packaged_backend_validation"] = packaged

    if rc == 0 and not packaged["ready"]:
        report["return_code"] = 21
        report["executable_validation"] = {
            "ready": False,
            "reason": "packaged_backend_validation_failed",
        }
    elif rc == 0 and not args.skip_exe_validation:
        report["executable_validation"] = validate_executable()
        if not report["executable_validation"]["ready"]:
            report["return_code"] = 20
    else:
        report["executable_validation"] = {"ready": False, "skipped": True}

    write_report(report)
    print(json.dumps(report, indent=2))
    return report["return_code"]


if __name__ == "__main__":
    raise SystemExit(main())
