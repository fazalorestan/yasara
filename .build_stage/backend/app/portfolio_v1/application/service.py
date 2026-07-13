from app.platform_core.service_registry.container import service_registry
from app.portfolio_v1.domain.models import PortfolioSnapshot
from app.portfolio_v1.engine.portfolio_engine import PortfolioIntelligenceEngineV1


class PortfolioIntelligenceServiceV1:
    def __init__(self, engine: PortfolioIntelligenceEngineV1 | None = None):
        self._engine = engine

    @property
    def engine(self) -> PortfolioIntelligenceEngineV1:
        if self._engine is None:
            self._engine = PortfolioIntelligenceEngineV1()
        return self._engine

    async def analyze(
        self,
        snapshot: PortfolioSnapshot,
        price_returns: dict[str, list[float]] | None = None,
        targets: dict[str, float] | None = None,
    ):
        return self.engine.analyze(snapshot, price_returns, targets)


def create_portfolio_intelligence_service_v1() -> PortfolioIntelligenceServiceV1:
    return PortfolioIntelligenceServiceV1()


if not service_registry.has("portfolio_intelligence_service_v1"):
    service_registry.register("portfolio_intelligence_service_v1", create_portfolio_intelligence_service_v1, singleton=True)


def get_portfolio_intelligence_service_v1() -> PortfolioIntelligenceServiceV1:
    return service_registry.resolve("portfolio_intelligence_service_v1")
