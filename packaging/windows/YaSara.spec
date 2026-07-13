# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
from PyInstaller.utils.hooks import (
    collect_submodules,
    collect_data_files,
    collect_dynamic_libs,
    copy_metadata,
)
import ast
import importlib.util
import os

project_root = Path.cwd()
stage_root = Path(os.environ.get("YASARA_BUILD_STAGE", project_root / ".build_stage"))
backend_source = stage_root / "backend"

datas = []
binaries = []
hiddenimports = set()

# Deterministic application data. Never package the whole frontend source or node_modules.
if backend_source.exists():
    datas.append((str(backend_source), "backend"))

frontend_dist = project_root / "frontend" / "dist"
if frontend_dist.exists():
    datas.append((str(frontend_dist), "frontend/dist"))

for folder in ["config", "plugins", "resources"]:
    path = project_root / folder
    if path.exists():
        datas.append((str(path), folder))

requirements_reference = project_root / "requirements.txt"

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


def discover_import_roots():
    roots = set()
    for folder in [backend_source, project_root / "desktop"]:
        if not folder.exists():
            continue
        for file in folder.rglob("*.py"):
            try:
                tree = ast.parse(
                    file.read_text(encoding="utf-8", errors="ignore")
                )
            except Exception:
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        roots.add(alias.name.split(".")[0])
                elif isinstance(node, ast.ImportFrom) and node.module:
                    roots.add(node.module.split(".")[0])
    return roots


def available(package):
    return importlib.util.find_spec(package) is not None


def add_package(package):
    if not available(package):
        return

    hiddenimports.add(package)

    try:
        hiddenimports.update(collect_submodules(package))
    except Exception:
        pass

    try:
        datas.extend(collect_data_files(package))
    except Exception:
        pass

    try:
        binaries.extend(collect_dynamic_libs(package))
    except Exception:
        pass

    try:
        datas.extend(copy_metadata(package))
    except Exception:
        pass


for root in discover_import_roots():
    if root in PACKAGE_MAP:
        add_package(PACKAGE_MAP[root])

for always in [
    "fastapi",
    "starlette",
    "pydantic",
    "pydantic_settings",
    "uvicorn",
    "anyio",
    "sqlalchemy",
    "apscheduler",
]:
    add_package(always)

# Explicit static-file imports required by the packaged FastAPI frontend host.
hiddenimports.update(
    {
        "fastapi.staticfiles",
        "starlette.staticfiles",
    }
)

entry = project_root / "desktop" / "yasara_desktop.py"
if not entry.exists():
    entry = project_root / "yasara.py"

a = Analysis(
    [str(entry)],
    pathex=[str(project_root), str(backend_source)],
    binaries=binaries,
    datas=datas,
    hiddenimports=sorted(hiddenimports),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="YaSara",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="YaSara",
)
