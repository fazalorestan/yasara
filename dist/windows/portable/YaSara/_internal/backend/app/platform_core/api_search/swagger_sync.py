from app.platform_core.api_search.catalog import api_search_catalog

class SwaggerSyncContract:
    def expected(self):
        endpoints = api_search_catalog.endpoints()
        return {
            "ready": True,
            "docs_url": "/docs",
            "openapi_url": "/openapi.json",
            "expected_endpoint_count": len(endpoints),
            "expected_paths": [item["path"] for item in endpoints],
            "sync_rule": "runtime_openapi_must_include_registered_paths",
        }

swagger_sync_contract = SwaggerSyncContract()
