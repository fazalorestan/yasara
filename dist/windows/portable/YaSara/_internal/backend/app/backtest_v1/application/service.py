from sqlalchemy.ext.asyncio import AsyncSession
from app.backtest_v1.domain.models import BacktestConfig
from app.backtest_v1.engine.backtest_engine import BacktestEngineV1
from app.backtest_v1.engine.monte_carlo import MonteCarloEngineV1
from app.backtest_v1.engine.walk_forward import WalkForwardEngineV1
from app.market_data.application.service import market_data_service
from app.market_data.application.sync_service import market_data_sync_service
from app.market_data.domain.models import ExchangeCode

class BacktestServiceV1:
    def __init__(self):
        self.engine = BacktestEngineV1()
        self.mc = MonteCarloEngineV1()
        self.walk = WalkForwardEngineV1()

    async def run_live(self, exchange: ExchangeCode, config: BacktestConfig, limit: int = 1000):
        candles = await market_data_service.candles(config.symbol, config.timeframe, limit, exchange)
        return self.engine.run(config, candles)

    async def run_stored(self, session: AsyncSession, exchange: ExchangeCode, config: BacktestConfig, limit: int = 1000):
        candles = await market_data_sync_service.stored_candles(session, config.symbol, config.timeframe, limit, exchange)
        return self.engine.run(config, candles)

    async def monte_carlo_live(self, exchange: ExchangeCode, config: BacktestConfig, limit: int = 1000, simulations: int = 500):
        report = await self.run_live(exchange, config, limit)
        return self.mc.simulate(config.initial_capital, report.trades, simulations)

    async def walk_forward_live(self, exchange: ExchangeCode, config: BacktestConfig, limit: int = 1500):
        candles = await market_data_service.candles(config.symbol, config.timeframe, limit, exchange)
        return self.walk.run(config, candles)

backtest_service_v1 = BacktestServiceV1()
