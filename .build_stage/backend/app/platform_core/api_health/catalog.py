class APIEndpointCatalog:
    def endpoints(self):
        return [
            {"path": "/api/v1/v5-0-alpha-14/license-readiness/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-14/license-readiness/gate", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-15/market-data/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-15/market-data/symbols", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-15/market-data/readiness", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-16/exchange-connector/summary", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-16/exchange-connector/list", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-16/exchange-connector/capabilities", "method": "GET", "critical": True},
            {"path": "/api/v1/v5-0-alpha-16/exchange-connector/readiness", "method": "GET", "critical": True},
        ]

api_endpoint_catalog = APIEndpointCatalog()
