class SwaggerVisibilityContract:
    def expected_visibility(self, prefix: str = "/api/v1"):
        return {
            "ready": True,
            "docs_url": "/docs",
            "openapi_url": "/openapi.json",
            "api_prefix": prefix,
            "visibility_rule": "registered_routers_must_appear_in_openapi_schema",
        }

swagger_visibility_contract = SwaggerVisibilityContract()
