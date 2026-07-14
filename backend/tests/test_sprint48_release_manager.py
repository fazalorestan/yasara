from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import pytest

from app.platform_core.release_manager.service import BUILD_ID, ReleaseManager
from app.platform_core.release_manager.tool_discovery import discover_tools


def test_release_manager_tool_contract():
    tools = discover_tools()
    assert set(tools) == {"git", "node", "npm", "python"}
    for value in tools.values():
        assert set(value) == {"available", "path", "version"}


def test_build_id_is_enterprise_sprint_48():
    assert re.fullmatch(r"2026\.48\.ENTERPRISE\.\d{3}", BUILD_ID)


def test_find_script_supports_root_and_scripts_directory(tmp_path: Path):
    manager = ReleaseManager(tmp_path)
    script = tmp_path / "finalize_dashboard.py"
    script.write_text("print('ok')", encoding="utf-8")
    assert manager._find_script("scripts/missing.py", "finalize_dashboard.py") == script


def test_find_script_optional_returns_none(tmp_path: Path):
    manager = ReleaseManager(tmp_path)
    assert manager._find_script("missing.py", required=False) is None


def test_atomic_report_write(tmp_path: Path):
    manager = ReleaseManager(tmp_path)
    manager._write({"ready": True})
    assert json.loads(manager.report_path.read_text(encoding="utf-8")) == {
        "ready": True
    }
    assert not manager.report_path.with_suffix(".json.tmp").exists()


def test_step_failure_is_logged_and_reported(tmp_path: Path):
    def runner(*args, **kwargs):
        return subprocess.CompletedProcess(args[0], 7, stdout="out", stderr="err")

    manager = ReleaseManager(tmp_path, runner=runner)
    report = {"steps": []}
    with pytest.raises(Exception, match="Release step failed"):
        manager._run("failure", ["tool", "arg"], tmp_path, report)

    assert report["steps"][0]["return_code"] == 7
    log = tmp_path / report["steps"][0]["log_file"]
    assert log.read_text(encoding="utf-8") == "out\nerr"


def test_diagnostics_contains_build_and_paths(tmp_path: Path):
    manager = ReleaseManager(tmp_path, timeout_seconds=99)
    diagnostics = manager.diagnostics()
    assert diagnostics["build_id"] == BUILD_ID
    assert diagnostics["timeout_seconds"] == 99
    assert Path(diagnostics["paths"]["frontend"]) == tmp_path / "frontend"
