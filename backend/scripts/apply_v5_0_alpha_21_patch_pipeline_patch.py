from pathlib import Path

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "v500_alpha21_patch_pipeline_v1" not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + "v500_alpha21_patch_pipeline_v1, ", 1)
    else:
        text = "from app.api.v1.routes import v500_alpha21_patch_pipeline_v1\n" + text
    text += "\napi_router.include_router(v500_alpha21_patch_pipeline_v1.router)\n"
router_file.write_text(text, encoding="utf-8")

yasara_file = Path("../yasara.py").resolve()
if yasara_file.exists():
    source = yasara_file.read_text(encoding="utf-8")
    if "AUTO_DISCOVER_V5_PATCHES" not in source:
        source = source.replace(
            "    for name in scripts:\n",
            "    # AUTO_DISCOVER_V5_PATCHES\n"
            "    backend_scripts = BACKEND / \"scripts\"\n"
            "    if backend_scripts.exists():\n"
            "        for patch_script in sorted(backend_scripts.glob(\"apply_v5_*.py\")):\n"
            "            if patch_script.name not in scripts:\n"
            "                scripts.append(patch_script.name)\n\n"
            "    for name in scripts:\n"
        )
        yasara_file.write_text(source, encoding="utf-8")
print("YaSara v5.0-alpha.21 Patch Pipeline patch applied.")
