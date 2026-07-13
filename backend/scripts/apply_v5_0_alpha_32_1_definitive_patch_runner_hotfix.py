from pathlib import Path

ROOT = Path("..").resolve()
yasara = ROOT / "yasara.py"
if not yasara.exists():
    raise SystemExit("yasara.py not found")

src = yasara.read_text(encoding="utf-8")

helper = '''def _yasara_patch_sort_key(name: str) -> tuple:
    import re
    m = re.search(r"apply_v(\\d+)_(\\d+)_alpha_(\\d+)", name)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)), name)
    m = re.search(r"apply_v(\\d+)_(\\d+)_(\\d+)", name)
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


'''

if "DEFINITIVE_PATCH_RUNNER_HOTFIX_V32_1" not in src:
    insert_at = src.find("def patch() -> None:")
    if insert_at == -1:
        raise SystemExit("patch() function not found")
    src = src[:insert_at] + helper + src[insert_at:]

if "for discovered_name in _yasara_discover_patch_scripts():" not in src:
    target = "    for name in scripts:\n"
    replacement = (
        "    for discovered_name in _yasara_discover_patch_scripts():\n"
        "        if discovered_name not in scripts:\n"
        "            scripts.append(discovered_name)\n\n"
        "    for name in scripts:\n"
    )
    if target not in src:
        raise SystemExit("patch loop not found")
    src = src.replace(target, replacement, 1)

yasara.write_text(src, encoding="utf-8")

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
module_name = "v500_alpha32_1_definitive_patch_runner_v1"
if module_name not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + module_name + ", ", 1)
    else:
        text = f"from app.api.v1.routes import {module_name}\n" + text
    text += f"\napi_router.include_router({module_name}.router)\n"
router_file.write_text(text, encoding="utf-8")

print("YaSara v5.0-alpha.32.1 Definitive Patch Runner hotfix applied.")
