from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Sequence

from .tool_discovery import discover_tools

BUILD_ID = "2026.48.ENTERPRISE.002"
DEFAULT_TIMEOUT_SECONDS = 60 * 60


class ReleaseError(RuntimeError):
    pass


@dataclass(frozen=True)
class StepResult:
    name: str
    success: bool
    return_code: int
    command: list[str]
    cwd: str
    duration_seconds: float
    log_file: str
    timed_out: bool = False


class ReleaseManager:
    """Validated YaSara release pipeline.

    The manager deliberately does not modify yasara.py. Existing command
    routing remains backward-compatible and imports this service through the
    already-installed release command.
    """

    def __init__(
        self,
        root: Path,
        *,
        runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
        timeout_seconds: int | None = None,
    ) -> None:
        self.root = Path(root).resolve()
        self.report_path = self.root / "runtime_reports" / "release_report.json"
        self.log_dir = self.root / "runtime_reports" / "release_logs"
        self.runner = runner
        self.timeout_seconds = timeout_seconds or int(
            os.getenv("YASARA_RELEASE_TIMEOUT_SECONDS", DEFAULT_TIMEOUT_SECONDS)
        )

    def _write(self, report: dict[str, object]) -> None:
        self.report_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.report_path.with_suffix(".json.tmp")
        temporary.write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        temporary.replace(self.report_path)

    def _find_script(self, *candidates: str, required: bool = True) -> Path | None:
        for candidate in candidates:
            path = self.root / candidate
            if path.is_file():
                return path
        if required:
            raise ReleaseError(
                "Required release script not found. Checked: "
                + ", ".join(candidates)
            )
        return None

    def _run(
        self,
        name: str,
        command: Sequence[str],
        cwd: Path,
        report: dict[str, object],
        *,
        timeout_seconds: int | None = None,
    ) -> subprocess.CompletedProcess[str]:
        normalized_command = [str(value) for value in command]
        print("\n>>>", " ".join(normalized_command), flush=True)
        started = time.monotonic()
        timed_out = False

        try:
            result = self.runner(
                normalized_command,
                cwd=str(cwd),
                text=True,
                shell=False,
                capture_output=True,
                timeout=timeout_seconds or self.timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            timed_out = True
            stdout = exc.stdout if isinstance(exc.stdout, str) else ""
            stderr = exc.stderr if isinstance(exc.stderr, str) else ""
            result = subprocess.CompletedProcess(
                normalized_command, 124, stdout=stdout, stderr=stderr
            )
        except OSError as exc:
            result = subprocess.CompletedProcess(
                normalized_command, 127, stdout="", stderr=str(exc)
            )

        duration = round(time.monotonic() - started, 3)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        step_number = len(report["steps"]) + 1  # type: ignore[arg-type]
        log_path = self.log_dir / f"{step_number:02d}_{name}.log"
        log_path.write_text(
            (result.stdout or "")
            + ("\n" if result.stdout and result.stderr else "")
            + (result.stderr or ""),
            encoding="utf-8",
        )

        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip(), file=sys.stderr)

        step = StepResult(
            name=name,
            success=result.returncode == 0,
            return_code=result.returncode,
            command=normalized_command,
            cwd=str(cwd),
            duration_seconds=duration,
            log_file=str(log_path.relative_to(self.root)),
            timed_out=timed_out,
        )
        report["steps"].append(asdict(step))  # type: ignore[union-attr]
        self._write(report)

        if result.returncode != 0:
            suffix = " (timeout)" if timed_out else ""
            raise ReleaseError(f"Release step failed: {name}{suffix}")
        return result

    def _capture(
        self,
        command: Sequence[str],
        cwd: Path | None = None,
        *,
        timeout_seconds: int = 30,
    ) -> str:
        result = self.runner(
            [str(value) for value in command],
            cwd=str(cwd or self.root),
            text=True,
            shell=False,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
        if result.returncode != 0:
            raise ReleaseError(
                (result.stderr or result.stdout or "Command failed").strip()
            )
        return (result.stdout or "").strip()

    def _staged_changes_exist(self, git: str) -> bool:
        result = self.runner(
            [git, "diff", "--cached", "--quiet"],
            cwd=str(self.root),
            text=True,
            shell=False,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if result.returncode not in (0, 1):
            raise ReleaseError("Unable to inspect staged Git changes.")
        return result.returncode == 1

    def diagnostics(self) -> dict[str, object]:
        tools = discover_tools()
        payload: dict[str, object] = {
            "build_id": BUILD_ID,
            "root": str(self.root),
            "tools": tools,
            "paths": {
                "frontend": str(self.root / "frontend"),
                "runtime_reports": str(self.root / "runtime_reports"),
            },
            "timeout_seconds": self.timeout_seconds,
        }
        path = self.root / "runtime_reports" / "release_diagnostics.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return payload

    def release(
        self,
        message: str | None = None,
        remote: str = "origin",
        branch: str | None = None,
        push: bool = True,
        skip_exe: bool = False,
        skip_dashboard: bool = False,
    ) -> int:
        tools = discover_tools()
        report: dict[str, object] = {
            "build_id": BUILD_ID,
            "started_at": dt.datetime.now().astimezone().isoformat(),
            "finished_at": None,
            "ready": False,
            "commit_created": False,
            "pushed": False,
            "branch": None,
            "remote": remote,
            "commit": None,
            "commit_message": None,
            "tools": tools,
            "steps": [],
        }

        try:
            required_tools = ("git", "node", "npm", "python")
            missing = [
                name
                for name in required_tools
                if not bool(tools.get(name, {}).get("available"))
            ]
            if missing:
                raise ReleaseError("Missing tools: " + ", ".join(missing))

            git = str(tools["git"]["path"])
            npm = str(tools["npm"]["path"])
            python = str(tools["python"]["path"])

            inside = self._capture([git, "rev-parse", "--is-inside-work-tree"])
            if inside.lower() != "true":
                raise ReleaseError("Current directory is not a Git repository.")

            resolved_branch = branch or self._capture(
                [git, "branch", "--show-current"]
            )
            if not resolved_branch:
                raise ReleaseError("Detached HEAD is not supported.")
            report["branch"] = resolved_branch

            if push:
                remotes = set(self._capture([git, "remote"]).split())
                if remote not in remotes:
                    raise ReleaseError(f"Git remote '{remote}' is not configured.")

            self._run("git_add", [git, "add", "--all"], self.root, report)
            if not self._staged_changes_exist(git):
                report.update(
                    {
                        "ready": True,
                        "reason": "nothing_to_commit",
                        "finished_at": dt.datetime.now().astimezone().isoformat(),
                    }
                )
                self._write(report)
                print("Nothing to commit.")
                return 0

            self._run(
                "git_diff_check",
                [git, "diff", "--cached", "--check"],
                self.root,
                report,
            )
            self._run(
                "tests", [python, "yasara.py", "test"], self.root, report
            )
            self._run(
                "frontend_build",
                [npm, "run", "build"],
                self.root / "frontend",
                report,
            )

            if not skip_exe:
                build_script = self._find_script(
                    "scripts/build_first_real_windows_exe.py",
                    "build_first_real_windows_exe.py",
                )
                executable_validator = self._find_script(
                    "scripts/check_yasara_executable_validation.py",
                    "check_yasara_executable_validation.py",
                )
                packaged_validator = self._find_script(
                    "scripts/verify_packaged_backend_snapshot.py",
                    "verify_packaged_backend_snapshot.py",
                    required=False,
                )

                self._run(
                    "windows_build",
                    [python, str(build_script), "--execute"],
                    self.root,
                    report,
                )
                if packaged_validator is not None:
                    self._run(
                        "packaged_backend_validation",
                        [python, str(packaged_validator)],
                        self.root,
                        report,
                    )
                self._run(
                    "executable_validation",
                    [python, str(executable_validator)],
                    self.root,
                    report,
                )

            if not skip_dashboard:
                dashboard_validator = self._find_script(
                    "scripts/validate_approved_dashboard_sprint47.py",
                    "scripts/validate_dashboard_stability.py",
                    "scripts/finalize_dashboard.py",
                    "finalize_dashboard.py",
                )
                self._run(
                    "dashboard_validation",
                    [python, str(dashboard_validator)],
                    self.root,
                    report,
                )

            self._run(
                "git_add_reports", [git, "add", "--all"], self.root, report
            )
            if not self._staged_changes_exist(git):
                report.update(
                    {
                        "ready": True,
                        "reason": "nothing_to_commit_after_validation",
                        "finished_at": dt.datetime.now().astimezone().isoformat(),
                    }
                )
                self._write(report)
                print("Validation passed; nothing to commit.")
                return 0

            commit_message = message or (
                "YaSara verified release "
                + dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
            )
            self._run(
                "git_commit",
                [git, "commit", "-m", commit_message],
                self.root,
                report,
            )
            report["commit_created"] = True
            report["commit_message"] = commit_message
            report["commit"] = self._capture([git, "rev-parse", "HEAD"])

            if push:
                self._run(
                    "git_push",
                    [git, "push", remote, resolved_branch],
                    self.root,
                    report,
                )
                report["pushed"] = True

            report["ready"] = True
            report["finished_at"] = dt.datetime.now().astimezone().isoformat()
            self._write(report)
            print("YaSara release completed successfully.")
            return 0
        except Exception as exc:
            report["error"] = str(exc)
            report["finished_at"] = dt.datetime.now().astimezone().isoformat()
            self._write(report)
            print(f"RELEASE FAILED: {exc}", file=sys.stderr)
            return 1
