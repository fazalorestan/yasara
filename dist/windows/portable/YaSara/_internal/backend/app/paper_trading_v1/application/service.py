from app.paper_trading_v1.domain.models import PaperAccount, PaperOrderRequest, PaperTradingState
from app.paper_trading_v1.engine.dashboard import PaperDashboardEngineV1
from app.paper_trading_v1.engine.order_manager import PaperOrderManagerV1

class PaperTradingServiceV1:
    def __init__(self):
        self.state = PaperTradingState(account=PaperAccount())
        self.orders = PaperOrderManagerV1()
        self.dashboard_engine = PaperDashboardEngineV1()

    async def reset(self, equity: float = 10000):
        self.state = PaperTradingState(account=PaperAccount(equity=equity, cash=equity))
        return self.state

    async def execute(self, request: PaperOrderRequest, market_price: float):
        return self.orders.execute_market_order(self.state, request, market_price)

    async def mark_to_market(self, prices: dict[str, float]):
        self.state = self.orders.mark_to_market(self.state, prices)
        return self.state

    async def dashboard(self):
        return self.dashboard_engine.build(self.state)

    async def get_state(self):
        return self.state

paper_trading_service_v1 = PaperTradingServiceV1()
