class RuntimeEndpointCatalog:
    def endpoints(self):
        return [
            {"path": "/api/v1/v5-0-alpha-20/api-search/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-21/patch-pipeline/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-22/broker-layer/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-23/risk-engine/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-23/risk-engine/contract", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-23/risk-engine/readiness", "method": "GET", "critical": True},
        ]

runtime_endpoint_catalog = RuntimeEndpointCatalog()
