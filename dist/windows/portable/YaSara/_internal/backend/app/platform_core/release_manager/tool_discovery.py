from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable

WINDOWS_DEFAULTS: dict[str, tuple[str, ...]] = {
    "git": (
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files\Git\bin\git.exe",
    ),
    "node": (
        r"C:\Program Files\nodejs\node.exe",
    ),
    "npm": (
        r"C:\Program Files\nodejs\npm.cmd",
        r"C:\Program Files\nodejs\npm.exe",
    ),
}

TOOL_CANDIDATES: dict[str, tuple[str, ...]] = {
    "git": ("git.exe", "git"),
    "node": ("node.exe", "node"),
    "npm": ("npm.cmd", "npm.exe", "npm"),
}


def _first_existing(candidates: Iterable[str]) -> str | None:
    for candidate in candidates:
        path = Path(candidate).expanduser()
        if path.is_file():
            return str(path.resolve())
    return None


def resolve_tool(name: str) -> str | None:
    """Resolve an executable without invoking a shell.

    Environment variables such as YASARA_GIT_PATH take priority, followed by
    PATH discovery and safe Windows fallback locations.
    """
    normalized = name.strip().lower()
    if normalized == "python":
        executable = Path(sys.executable)
        return str(executable.resolve()) if executable.is_file() else None

    if normalized not in TOOL_CANDIDATES:
        raise ValueError(f"Unsupported tool: {name}")

    override = os.getenv(f"YASARA_{normalized.upper()}_PATH")
    if override:
        resolved = _first_existing((override,))
        if resolved:
            return resolved

    for candidate in TOOL_CANDIDATES[normalized]:
        found = shutil.which(candidate)
        if found:
            return str(Path(found).resolve())

    return _first_existing(WINDOWS_DEFAULTS.get(normalized, ()))


def tool_version(path: str | None, timeout_seconds: int = 15) -> str | None:
    if not path:
        return None
    try:
        result = subprocess.run(
            [path, "--version"],
            text=True,
            shell=False,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None

    text = (result.stdout or result.stderr or "").strip()
    return text.splitlines()[0] if text else None


def discover_tools() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for name in ("git", "node", "npm", "python"):
        path = resolve_tool(name)
        result[name] = {
            "available": bool(path),
            "path": path,
            "version": tool_version(path),
        }
    return result
