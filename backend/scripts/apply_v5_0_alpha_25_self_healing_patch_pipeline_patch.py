from pathlib import Path
router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "v500_alpha25_self_healing_patch_pipeline_v1" not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + "v500_alpha25_self_healing_patch_pipeline_v1, ", 1)
    else:
        text = "from app.api.v1.routes import v500_alpha25_self_healing_patch_pipeline_v1\n" + text
    text += "\napi_router.include_router(v500_alpha25_self_healing_patch_pipeline_v1.router)\n"
router_file.write_text(text, encoding="utf-8")
yasara_file = Path("../yasara.py").resolve()
if yasara_file.exists():
    source = yasara_file.read_text(encoding="utf-8")
    if "SELF_HEALING_PATCH_PIPELINE_V25" not in source:
        source = source.replace(
            "def patch() -> None:\n",
            "def _discover_patch_scripts() -> list[str]:\n"
            "    # SELF_HEALING_PATCH_PIPELINE_V25\n"
            "    discovered = []\n"
            "    for folder in [BACKEND / \"scripts\", ROOT / \"scripts\"]:\n"
            "        if folder.exists():\n"
            "            discovered.extend(p.name for p in folder.glob(\"apply_v*.py\"))\n"
            "    return sorted(set(discovered))\n\n"
            "def patch() -> None:\n"
        )
        source = source.replace(
            "    for name in scripts:\n",
            "    for discovered_name in _discover_patch_scripts():\n"
            "        if discovered_name not in scripts:\n"
            "            scripts.append(discovered_name)\n\n"
            "    for name in scripts:\n"
        )
        yasara_file.write_text(source, encoding="utf-8")
print("YaSara v5.0-alpha.25 Self-Healing Patch Pipeline patch applied.")
