class RouterEndpointManifestContract:
    def build(self, route_modules: list[dict]):
        return {
            "ready": True,
            "total": len(route_modules),
            "modules": [
                {"module_name": item["module_name"], "import_path": item["import_path"], "registered": item.get("ready", False)}
                for item in route_modules
            ],
        }

router_endpoint_manifest_contract = RouterEndpointManifestContract()
