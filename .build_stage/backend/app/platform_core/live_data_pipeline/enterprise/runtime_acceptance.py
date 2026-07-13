class LiveDataEnterpriseRuntimeAcceptance:
    def contract(self):
        return {
            "ready": True,
            "required_runtime_endpoints": [
                "/api/v1/v5-0-alpha-39/live-data-core/summary",
                "/api/v1/v5-0-alpha-39/live-stream-manager/summary",
                "/api/v1/v5-0-alpha-39/live-data-cache/summary",
                "/api/v1/v5-0-alpha-39/live-data-enterprise/summary",
            ],
            "requires_http_200": True,
            "auto_router_registry_required": True,
            "manual_apply_required": False,
            "real_connection": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

live_data_enterprise_runtime_acceptance = LiveDataEnterpriseRuntimeAcceptance()
