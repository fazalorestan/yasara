import importlib

class RouteModuleImporter:
    def inspect(self, import_path: str):
        try:
            module = importlib.import_module(import_path)
            router = getattr(module, "router", None)
            return {"ready": router is not None, "import_path": import_path, "has_router": router is not None, "error": None}
        except Exception as exc:
            return {"ready": False, "import_path": import_path, "has_router": False, "error": str(exc)}

route_module_importer = RouteModuleImporter()
