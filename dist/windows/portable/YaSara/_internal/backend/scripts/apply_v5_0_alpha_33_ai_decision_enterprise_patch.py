from pathlib import Path
router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
module_name = "v500_alpha33_ai_decision_enterprise_v1"
if module_name not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + module_name + ", ", 1)
    else:
        text = f"from app.api.v1.routes import {module_name}\n" + text
    text += f"\napi_router.include_router({module_name}.router)\n"
router_file.write_text(text, encoding="utf-8")
print("YaSara v5.0-alpha.33 AI Decision Enterprise patch applied.")
