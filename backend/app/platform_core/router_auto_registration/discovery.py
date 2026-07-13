from pathlib import Path

class RouteModuleDiscovery:
    def __init__(self, routes_dir: str = "app/api/v1/routes"):
        self.routes_dir = Path(routes_dir)

    def discover(self):
        if not self.routes_dir.exists():
            return []
        modules = []
        for path in sorted(self.routes_dir.glob("*.py")):
            if path.name == "__init__.py" or path.name.startswith("_"):
                continue
            modules.append({
                "module_name": path.stem,
                "import_path": ".".join(path.with_suffix("").parts),
                "file": str(path),
            })
        return modules

route_module_discovery = RouteModuleDiscovery()
