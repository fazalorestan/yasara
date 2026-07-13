from pathlib import Path

main_file = Path("app/main.py")
text = main_file.read_text(encoding="utf-8")

if "StaticFiles" not in text:
    text = text.replace("from fastapi import FastAPI", "from fastapi import FastAPI\nfrom fastapi.staticfiles import StaticFiles\nfrom fastapi.responses import FileResponse")

if "app.mount(\"/static\"" not in text:
    text += "\n\napp.mount(\"/static\", StaticFiles(directory=\"app/static\"), name=\"static\")\n"

if "def yasara_dashboard_app" not in text:
    text += '''
@app.get("/app", include_in_schema=False)
async def yasara_dashboard_app():
    return FileResponse("app/static/dashboard/index.html")
'''

main_file.write_text(text, encoding="utf-8")

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
if "v12_dashboard_shell_v1" not in text:
    if "from app.api.v1.routes import" in text:
        text = text.replace("from app.api.v1.routes import", "from app.api.v1.routes import v12_dashboard_shell_v1,")
    else:
        text = "from app.api.v1.routes import v12_dashboard_shell_v1\n" + text
    text += "\napi_router.include_router(v12_dashboard_shell_v1.router)\n"
router_file.write_text(text, encoding="utf-8")

print("YaSara v1.2 Phase 1 Dashboard Shell patch applied.")
