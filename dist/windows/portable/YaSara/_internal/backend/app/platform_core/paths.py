from __future__ import annotations
from pathlib import Path

def backend_root() -> Path:
    return Path(__file__).resolve().parents[2]

def project_root() -> Path:
    return backend_root().parent

def frontend_root() -> Path:
    return project_root() / "frontend"

def data_root() -> Path:
    return project_root() / "data"

def docs_root() -> Path:
    return project_root() / "docs"

def plugin_manifest_root() -> Path:
    return data_root() / "plugin_manifests"

def ensure_platform_dirs() -> dict[str, str]:
    roots = {
        "project_root": project_root(),
        "backend_root": backend_root(),
        "frontend_root": frontend_root(),
        "data_root": data_root(),
        "docs_root": docs_root(),
        "plugin_manifest_root": plugin_manifest_root(),
    }
    data_root().mkdir(parents=True, exist_ok=True)
    plugin_manifest_root().mkdir(parents=True, exist_ok=True)
    return {k: str(v) for k, v in roots.items()}
