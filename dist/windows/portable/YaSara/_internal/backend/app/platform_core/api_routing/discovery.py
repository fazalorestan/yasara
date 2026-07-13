from pathlib import Path

class AutoRouterDiscovery:
    def __init__(self, routes_dir: str = "app/api/v1/routes"):
        self.routes_dir = Path(routes_dir)

    def discover_files(self):
        if not self.routes_dir.exists():
            return []
        return sorted([p for p in self.routes_dir.glob("*.py") if p.name != "__init__.py" and not p.name.startswith("_")])

    def discover_modules(self):
        modules = []
        for path in self.discover_files():
            modules.append({
                "module_name": path.stem,
                "import_path": ".".join(path.with_suffix("").parts),
                "has_router": True,
                "safe_to_register": True,
            })
        return modules

auto_router_discovery = AutoRouterDiscovery()
