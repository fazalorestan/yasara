from app.v11_operations.models import ProjectInfoV11


class ProjectInfoBuilderV11:
    def build(self) -> ProjectInfoV11:
        return ProjectInfoV11(modules=[
            "v11_market_data",
            "v11_exchange_connectivity",
            "v11_ai_market_intelligence",
            "v11_dashboard_runtime",
            "v11_operations",
        ])
