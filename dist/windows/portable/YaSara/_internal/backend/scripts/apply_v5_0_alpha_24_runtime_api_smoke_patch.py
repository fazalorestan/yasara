from pathlib import Path
router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "v500_alpha24_runtime_api_smoke_v1" not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + "v500_alpha24_runtime_api_smoke_v1, ", 1)
    else:
        text = "from app.api.v1.routes import v500_alpha24_runtime_api_smoke_v1\n" + text
    text += "\napi_router.include_router(v500_alpha24_runtime_api_smoke_v1.router)\n"
router_file.write_text(text, encoding="utf-8")
print("YaSara v5.0-alpha.24 Runtime API Smoke patch applied.")
