from pathlib import Path

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "v11_risk_control_v1" not in text:
    if "from app.api.v1.routes import" in text:
        text = text.replace("from app.api.v1.routes import", "from app.api.v1.routes import v11_risk_control_v1,")
    else:
        text = "from app.api.v1.routes import v11_risk_control_v1\n" + text
    text += "\napi_router.include_router(v11_risk_control_v1.router)\n"
router_file.write_text(text, encoding="utf-8")
print("YaSara v1.1 Phase 7 Risk Control router patch applied.")
