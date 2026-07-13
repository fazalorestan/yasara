from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "runtime_reports/release_report.json"
BUILD_ID = "2026.47.RELEASE.001"


class ReleaseError(RuntimeError):
    pass


def run(cmd, cwd=ROOT, check=True, capture=False):
    print("\n>>>", " ".join(cmd))
    result = subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        shell=False,
        capture_output=capture,
    )
    if capture:
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip(), file=sys.stderr)
    if check and result.returncode:
        raise ReleaseError(
            f"Command failed ({result.returncode}): {' '.join(cmd)}"
        )
    return result


def require(name: str) -> None:
    if shutil.which(name) is None:
        raise ReleaseError(f"Required tool not found: {name}")


def find_script(*candidates: str):
    for candidate in candidates:
        path = ROOT / candidate
        if path.exists():
            return path
    return None


def run_python(path: Path, *args: str) -> None:
    run([sys.executable, str(path), *args])


def staged_changes_exist() -> bool:
    result = run(["git", "diff", "--cached", "--quiet"], check=False)
    return result.returncode == 1


def write_report(payload: dict) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate, commit, and push a verified YaSara release."
    )
    parser.add_argument("-m", "--message")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch")
    parser.add_argument("--no-push", action="store_true")
    parser.add_argument("--skip-exe", action="store_true")
    parser.add_argument("--skip-dashboard", action="store_true")
    args = parser.parse_args()

    report = {
        "build_id": BUILD_ID,
        "ready": False,
        "commit_created": False,
        "pushed": False,
        "steps": {},
    }

    try:
        require("git")
        require("npm")

        inside = run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture=True,
        ).stdout.strip()
        if inside != "true":
            raise ReleaseError("Current directory is not a Git repository.")

        branch = args.branch or run(
            ["git", "branch", "--show-current"],
            capture=True,
        ).stdout.strip()
        if not branch:
            raise ReleaseError("Detached HEAD is not allowed.")

        report["branch"] = branch
        report["remote"] = args.remote

        if not args.no_push:
            remotes = set(run(["git", "remote"], capture=True).stdout.split())
            if args.remote not in remotes:
                raise ReleaseError(
                    f"Git remote '{args.remote}' is not configured."
                )

        run(["git", "add", "--all"])
        report["steps"]["git_add"] = True

        if not staged_changes_exist():
            report.update({"ready": True, "reason": "nothing_to_commit"})
            write_report(report)
            print("Nothing to commit.")
            return 0

        run(["git", "diff", "--cached", "--check"])
        report["steps"]["git_diff_check"] = True

        run([sys.executable, "yasara.py", "test"])
        report["steps"]["tests"] = True

        run(["npm", "run", "build"], cwd=ROOT / "frontend")
        report["steps"]["frontend_build"] = True

        if not args.skip_exe:
            build = find_script(
                "scripts/build_first_real_windows_exe.py",
                "build_first_real_windows_exe.py",
            )
            check = find_script(
                "scripts/check_yasara_executable_validation.py",
                "check_yasara_executable_validation.py",
            )
            if build is None or check is None:
                raise ReleaseError(
                    "Executable build or validation script is missing."
                )

            run_python(build, "--execute")
            report["steps"]["windows_build"] = True

            packaged = find_script(
                "scripts/verify_packaged_backend_snapshot.py"
            )
            if packaged is not None:
                run_python(packaged)
                report["steps"]["packaged_backend_validation"] = True

            run_python(check)
            report["steps"]["executable_validation"] = True

        if not args.skip_dashboard:
            dashboard = find_script(
                "scripts/validate_approved_dashboard_sprint47.py",
                "scripts/validate_dashboard_stability.py",
                "scripts/finalize_dashboard.py",
                "finalize_dashboard.py",
            )
            if dashboard is None:
                raise ReleaseError("Dashboard validation script is missing.")
            run_python(dashboard)
            report["steps"]["dashboard_validation"] = True

        run(["git", "add", "--all"])

        if not staged_changes_exist():
            report.update(
                {"ready": True, "reason": "nothing_to_commit_after_validation"}
            )
            write_report(report)
            print("Validation passed; nothing to commit.")
            return 0

        message = args.message or (
            "YaSara verified release "
            + dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
        )
        run(["git", "commit", "-m", message])
        report["commit_created"] = True
        report["commit_message"] = message
        report["commit"] = run(
            ["git", "rev-parse", "HEAD"],
            capture=True,
        ).stdout.strip()

        if not args.no_push:
            run(["git", "push", args.remote, branch])
            report["pushed"] = True

        report["ready"] = True
        write_report(report)
        print("YaSara release completed successfully.")
        return 0

    except Exception as exc:
        report["error"] = str(exc)
        write_report(report)
        print(f"RELEASE FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
