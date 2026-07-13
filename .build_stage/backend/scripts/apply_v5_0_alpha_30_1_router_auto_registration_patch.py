from pathlib import Path

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
module_name = "v500_alpha30_1_router_auto_registration_v1"

if module_name not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + module_name + ", ", 1)
    else:
        text = f"from app.api.v1.routes import {module_name}\n" + text
    text += f"\napi_router.include_router({module_name}.router)\n"

router_file.write_text(text, encoding="utf-8")

# Strengthen yasara.py patch discovery.
yasara_file = Path("../yasara.py").resolve()
if yasara_file.exists():
    src = yasara_file.read_text(encoding="utf-8")
    if "ROUTER_AUTO_REGISTRATION_ENGINE_30_1" not in src:
        if "def _discover_patch_scripts()" not in src:
            src = src.replace(
                "def patch() -> None:\n",
                "def _discover_patch_scripts() -> list[str]:\n"
                "    # ROUTER_AUTO_REGISTRATION_ENGINE_30_1\n"
                "    discovered = []\n"
                "    for folder in [BACKEND / \"scripts\", ROOT / \"scripts\"]:\n"
                "        if folder.exists():\n"
                "            discovered.extend(p.name for p in folder.glob(\"apply_v*.py\"))\n"
                "    return sorted(set(discovered))\n\n"
                "def patch() -> None:\n"
            )
        if "for discovered_name in _discover_patch_scripts()" not in src:
            src = src.replace(
                "    for name in scripts:\n",
                "    for discovered_name in _discover_patch_scripts():\n"
                "        if discovered_name not in scripts:\n"
                "            scripts.append(discovered_name)\n\n"
                "    for name in scripts:\n"
            )
        yasara_file.write_text(src, encoding="utf-8")

print("YaSara v5.0-alpha.30.1 Router Auto Registration patch applied.")
