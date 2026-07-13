from app.platform_core.diagnostics.models import DiagnosticCheck
from app.platform_core.paths import backend_root, data_root, docs_root, frontend_root, plugin_manifest_root, project_root

class PathIntegrityCheck:
    def run(self):
        paths = {
            "project_root": project_root(),
            "backend_root": backend_root(),
            "frontend_root": frontend_root(),
            "data_root": data_root(),
            "docs_root": docs_root(),
            "plugin_manifest_root": plugin_manifest_root(),
        }
        missing = [name for name, path in paths.items() if not path.exists()]
        return DiagnosticCheck(
            name="path_integrity",
            ready=len(missing) == 0,
            severity="error" if missing else "info",
            detail="all core paths exist" if not missing else "some core paths are missing",
            data={k: str(v) for k, v in paths.items()} | {"missing": missing},
        )
