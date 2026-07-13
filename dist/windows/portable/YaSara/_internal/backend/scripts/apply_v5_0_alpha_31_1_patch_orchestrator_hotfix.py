from pathlib import Path

ROOT = Path("..").resolve()
yasara_file = ROOT / "yasara.py"
if not yasara_file.exists():
    raise SystemExit("yasara.py not found")

src = yasara_file.read_text(encoding="utf-8")

helper = '''def _yasara_discover_all_patch_scripts() -> list[str]:
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


'''

if "PATCH_ORCHESTRATOR_HOTFIX_V31_1" not in src:
    src = src.replace("def patch() -> None:\n", helper + "def patch() -> None:\n")

if "for discovered_name in _yasara_discover_all_patch_scripts():" not in src:
    src = src.replace(
        "    for name in scripts:\n",
        "    for discovered_name in _yasara_discover_all_patch_scripts():\n"
        "        if discovered_name not in scripts:\n"
        "            scripts.append(discovered_name)\n\n"
        "    for name in scripts:\n",
        1,
    )

yasara_file.write_text(src, encoding="utf-8")

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
module_name = "v500_alpha31_1_patch_orchestrator_v1"
if module_name not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + module_name + ", ", 1)
    else:
        text = f"from app.api.v1.routes import {module_name}\n" + text
    text += f"\napi_router.include_router({module_name}.router)\n"
router_file.write_text(text, encoding="utf-8")

print("YaSara v5.0-alpha.31.1 Patch Orchestrator hotfix applied.")
