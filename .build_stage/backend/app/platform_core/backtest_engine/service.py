from app.platform_core.backtest_engine.config import backtest_config_service
from app.platform_core.backtest_engine.dataset import historical_dataset_contract
from app.platform_core.backtest_engine.report import backtest_report_builder
from app.platform_core.backtest_engine.signal_simulator import backtest_signal_simulator
from app.platform_core.backtest_engine.trade_simulator import trade_simulation_engine

class BacktestEngineFoundationService:
    def config(self): return backtest_config_service.default()
    def dataset(self): return historical_dataset_contract.sample()
    def signals(self):
        data = historical_dataset_contract.sample()
        return backtest_signal_simulator.generate(data["candles"])
    def trades(self):
        data = historical_dataset_contract.sample()
        signals = backtest_signal_simulator.generate(data["candles"])
        return trade_simulation_engine.simulate(data["symbol"], signals["signals"])
    def report(self):
        cfg = backtest_config_service.default()
        trades = self.trades()
        return backtest_report_builder.build(trades["trades"], cfg["initial_equity"])
    def run(self):
        report = self.report()
        return {"ready": True, "report": report, "execution_allowed": False}

backtest_engine_foundation_service = BacktestEngineFoundationService()
