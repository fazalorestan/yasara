from pathlib import Path
router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "v450_indicator_platform_handoff_v1" not in text:
    if "from app.api.v1.routes import" in text:
        text = text.replace("from app.api.v1.routes import", "from app.api.v1.routes import v450_indicator_platform_handoff_v1,")
    else:
        text = "from app.api.v1.routes import v450_indicator_platform_handoff_v1\n" + text
    text += "\napi_router.include_router(v450_indicator_platform_handoff_v1.router)\n"
router_file.write_text(text, encoding="utf-8")
print("YaSara v4.50 Indicator Platform Handoff router patch applied.")
