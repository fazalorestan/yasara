from app.platform_core.backtest_engine.readiness import backtest_engine_readiness_gate
from app.platform_core.backtest_engine.service import backtest_engine_foundation_service
from app.v500_alpha29_backtest_engine.models import BacktestEngineSummaryV500Alpha29

class BacktestEngineFacadeV500Alpha29:
    def summary(self): return BacktestEngineSummaryV500Alpha29()
    def config(self): return backtest_engine_foundation_service.config()
    def dataset(self): return backtest_engine_foundation_service.dataset()
    def signals(self): return backtest_engine_foundation_service.signals()
    def trades(self): return backtest_engine_foundation_service.trades()
    def report(self): return backtest_engine_foundation_service.report()
    def run(self): return backtest_engine_foundation_service.run()
    def readiness(self): return backtest_engine_readiness_gate.run()
    def contract(self): return {"ready": True, "backtest_engine": "foundation_only", "requires_market_data": True, "requires_strategy_engine": True, "execution_allowed": False}
