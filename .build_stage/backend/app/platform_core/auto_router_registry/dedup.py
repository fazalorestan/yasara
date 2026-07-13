class AutoRouterDedupService:
    def route_signature(self, route) -> tuple:
        return (getattr(route, "path", ""), tuple(sorted(getattr(route, "methods", []) or [])))

    def existing_signatures(self, api_router) -> set:
        return {self.route_signature(route) for route in getattr(api_router, "routes", [])}

    def router_signatures(self, router) -> set:
        return {self.route_signature(route) for route in getattr(router, "routes", [])}

    def should_include(self, api_router, router) -> bool:
        incoming = self.router_signatures(router)
        if not incoming:
            return False
        return not bool(self.existing_signatures(api_router).intersection(incoming))

auto_router_dedup_service = AutoRouterDedupService()
