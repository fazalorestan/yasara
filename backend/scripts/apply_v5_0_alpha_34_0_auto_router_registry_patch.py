from pathlib import Path

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
module_name = "v500_alpha34_0_auto_router_registry_v1"

if module_name not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + module_name + ", ", 1)
    else:
        text = f"from app.api.v1.routes import {module_name}\n" + text
    text += f"\napi_router.include_router({module_name}.router)\n"

auto_block = """
# AUTO_ROUTER_REGISTRY_V34_0_START
try:
    from app.platform_core.auto_router_registry.registry import auto_router_registry
    AUTO_ROUTER_REGISTRY_RESULT = auto_router_registry.register_all(api_router)
except Exception as exc:
    AUTO_ROUTER_REGISTRY_RESULT = {"ready": False, "error": str(exc), "registered_count": 0, "failed_count": 1}
# AUTO_ROUTER_REGISTRY_V34_0_END
"""

if "AUTO_ROUTER_REGISTRY_V34_0_START" not in text:
    text += "\\n" + auto_block + "\\n"

router_file.write_text(text, encoding="utf-8")
print("YaSara v5.0-alpha.34.0 Auto Router Registry patch applied.")
