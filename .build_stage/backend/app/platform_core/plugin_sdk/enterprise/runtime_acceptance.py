class PluginEnterpriseRuntimeAcceptance:
    def contract(self):
        return {
            "ready": True,
            "required_runtime_endpoints": [
                "/api/v1/v5-0-alpha-36/plugin-sdk-core/summary",
                "/api/v1/v5-0-alpha-36/plugin-runtime-sandbox/summary",
                "/api/v1/v5-0-alpha-36/plugin-versioning/summary",
                "/api/v1/v5-0-alpha-36/plugin-enterprise/summary",
            ],
            "requires_http_200": True,
            "auto_router_registry_required": True,
            "manual_apply_required": False,
            "execution_allowed": False,
        }

plugin_enterprise_runtime_acceptance = PluginEnterpriseRuntimeAcceptance()
