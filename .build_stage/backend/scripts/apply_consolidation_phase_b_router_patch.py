from pathlib import Path

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "consolidation_phase_b_v1" not in text:
    if "from app.api.v1.routes import" in text:
        text = text.replace("from app.api.v1.routes import", "from app.api.v1.routes import consolidation_phase_b_v1,")
    else:
        text = "from app.api.v1.routes import consolidation_phase_b_v1\n" + text
    text += "\napi_router.include_router(consolidation_phase_b_v1.router)\n"
router_file.write_text(text, encoding="utf-8")
print("Consolidation Phase B router patch applied.")
