import importlib

class SafeRouterRegistrar:
    def import_router(self, import_path: str):
        module = importlib.import_module(import_path)
        router = getattr(module, "router", None)
        return {"ready": router is not None, "import_path": import_path, "has_router": router is not None, "router": router}

    def dry_run(self, records: list[dict]):
        results = []
        for record in records:
            try:
                imported = self.import_router(record["import_path"])
                results.append({k: v for k, v in imported.items() if k != "router"})
            except Exception as exc:
                results.append({"ready": False, "import_path": record.get("import_path"), "has_router": False, "error": str(exc)})
        return {"ready": all(r["ready"] for r in results), "results": results, "mode": "dry_run_only"}

safe_router_registrar = SafeRouterRegistrar()
