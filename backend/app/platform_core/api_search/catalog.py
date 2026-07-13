class APISearchCatalog:
    def endpoints(self):
        return [
            {"path": "/api/v1/health", "tag": "health", "summary": "Health"},
            {"path": "/api/v1/v5-0-alpha-16/exchange-connector/summary", "tag": "exchange", "summary": "Exchange Connector Summary"},
            {"path": "/api/v1/v5-0-alpha-17/api-health/summary", "tag": "api-health", "summary": "API Health Summary"},
            {"path": "/api/v1/v5-0-alpha-18/exchange-sdk/summary", "tag": "exchange-sdk", "summary": "Exchange SDK Summary"},
            {"path": "/api/v1/v5-0-alpha-19/auto-router/summary", "tag": "auto-router", "summary": "Auto Router Summary"},
            {"path": "/api/v1/v5-0-alpha-20/api-search/summary", "tag": "api-search", "summary": "API Search Summary"},
        ]

api_search_catalog = APISearchCatalog()
