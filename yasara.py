from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"


def run(cmd: list[str], cwd: Path | None = None, env: dict | None = None) -> int:
    print(f"\n[YaSara] {cwd or ROOT}> {' '.join(cmd)}")
    completed = subprocess.run(cmd, cwd=str(cwd or ROOT), env=env)
    return int(completed.returncode)


def _discover_patch_scripts() -> list[str]:
    # SELF_HEALING_PATCH_PIPELINE_V25
    discovered = []
    for folder in [BACKEND / "scripts", ROOT / "scripts"]:
        if folder.exists():
            discovered.extend(p.name for p in folder.glob("apply_v*.py"))
    return sorted(set(discovered))

def _yasara_discover_all_patch_scripts() -> list[str]:
    # PATCH_ORCHESTRATOR_HOTFIX_V31_1
    discovered: list[str] = []
    for folder in [BACKEND / "scripts", ROOT / "scripts"]:
        if folder.exists():
            for item in folder.glob("apply_v*.py"):
                if item.is_file():
                    name = item.name
                    lowered = name.lower()
                    blocked = any(x in lowered for x in ["delete", "wipe", "drop", "remove_all", "format"])
                    if name.startswith("apply_v") and name.endswith(".py") and not blocked:
                        discovered.append(name)
    return sorted(set(discovered))


def _yasara_patch_sort_key(name: str) -> tuple:
    import re
    m = re.search(r"apply_v(\d+)_(\d+)_alpha_(\d+)", name)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)), name)
    m = re.search(r"apply_v(\d+)_(\d+)_(\d+)", name)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)), name)
    return (0, 0, 0, name)


def _yasara_discover_patch_scripts() -> list[str]:
    # DEFINITIVE_PATCH_RUNNER_HOTFIX_V32_1
    discovered: list[str] = []
    for folder in [BACKEND / "scripts", ROOT / "scripts"]:
        if folder.exists():
            for item in folder.glob("apply_v*.py"):
                if not item.is_file():
                    continue
                name = item.name
                lowered = name.lower()
                blocked = any(x in lowered for x in ["delete", "wipe", "drop", "remove_all", "format"])
                if name.startswith("apply_v") and name.endswith(".py") and not blocked:
                    discovered.append(name)
    return sorted(set(discovered), key=_yasara_patch_sort_key)


def patch() -> None:
    # SIMPLE_PATCH_RUNNER_FIX_V33_1
    scripts = [
        "apply_v4_18_launcher_router_patch.py",
        "sync_operational_frontend_status.py",
        "apply_v4_17_elliott_router_patch.py",
        "apply_v4_16_neowave_sprint2_router_patch.py",
        "apply_v4_15_neowave_router_patch.py",
        "apply_v4_14_ai_fusion_router_patch.py",
        "apply_v4_13_ict_engine_router_patch.py",
        "apply_v4_12_smart_money_pro_sprint2_router_patch.py",
        "apply_v4_11_smart_money_pro_router_patch.py",
        "apply_v4_10_market_structure_sprint2_router_patch.py",
        "apply_v4_9_market_structure_router_patch.py",
        "apply_v4_8_production_readiness_router_patch.py",
        "apply_v4_7_notification_alerts_router_patch.py",
        "apply_v4_6_trading_journal_router_patch.py",
        "apply_v4_5_paper_trading_router_patch.py",
        "apply_v4_4_backtest_benchmark_router_patch.py",
        "apply_v4_3_risk_engine_router_patch.py",
        "apply_v4_2_signal_engine_router_patch.py",
        "apply_v4_1_indicator_engine_router_patch.py",
        "apply_v4_0_market_context_router_patch.py",
        "apply_v3_6_1_phase_a_guardrails_router_patch.py",
    ]

    for folder in [BACKEND / "scripts", ROOT / "scripts"]:
        if folder.exists():
            for item in folder.glob("apply_v*.py"):
                if item.is_file():
                    name = item.name
                    lowered = name.lower()
                    blocked = any(x in lowered for x in ["delete", "wipe", "drop", "remove_all", "format"])
                    if name.startswith("apply_v") and name.endswith(".py") and not blocked and name not in scripts:
                        scripts.append(name)

    scripts = list(dict.fromkeys(scripts))

    for name in scripts:
        path = BACKEND / "scripts" / name
        root_path = ROOT / "scripts" / name
        if path.exists():
            code = run([sys.executable, str(path)], cwd=BACKEND)
            if code != 0:
                raise SystemExit(code)
        elif root_path.exists():
            code = run([sys.executable, str(root_path)], cwd=ROOT)
            if code != 0:
                raise SystemExit(code)

    print("\n[YaSara] Patch flow completed successfully.")

def test() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BACKEND)
    code = run([sys.executable, "-m", "pytest", "tests"], cwd=BACKEND, env=env)
    raise SystemExit(code)


def run_backend() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BACKEND)
    code = run([
        sys.executable,
        "-m",
        "uvicorn",
        "app.main:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000",
        "--reload",
    ], cwd=BACKEND, env=env)
    raise SystemExit(code)


def run_frontend() -> None:
    npm = "npm.cmd" if os.name == "nt" else "npm"
    if not FRONTEND.exists():
        raise SystemExit("frontend folder not found")
    code = run([npm, "run", "dev"], cwd=FRONTEND)
    raise SystemExit(code)


def start() -> None:
    try:
        from scripts.yasara_one_command_launcher import start as launcher_start
    except Exception as exc:
        raise SystemExit(f"Launcher module not available: {exc}")
    launcher_start(open_browser=True)


def main() -> None:
    parser = argparse.ArgumentParser(prog="yasara.py")
    parser.add_argument(
        "command",
        choices=["patch", "test", "run-backend", "run-frontend", "start"],
    )
    args = parser.parse_args()

    if args.command == "patch":
        patch()
    elif args.command == "test":
        test()
    elif args.command == "run-backend":
        run_backend()
    elif args.command == "run-frontend":
        run_frontend()
    elif args.command == "start":
        start()


if __name__ == "__main__":
    main()
