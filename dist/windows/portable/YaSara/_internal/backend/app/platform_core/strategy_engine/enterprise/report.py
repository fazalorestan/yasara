from app.platform_core.strategy_engine.allocation_report import strategy_allocation_report
from app.platform_core.strategy_engine.report import strategy_core_report
from app.platform_core.strategy_engine.scoring_report import strategy_scoring_report
from app.platform_core.strategy_engine.simulation_report import strategy_simulation_report

class StrategyEnterpriseReportBuilder:
    def build(self):
        return {
            "ready": True,
            "sprint": "v5.0-alpha.41",
            "name": "Strategy Engine",
            "packages": [
                "A-Strategy-Core-Contract",
                "B-Signal-Scoring",
                "C-Portfolio-Allocation",
                "D-Backtest-Simulation",
                "E-Enterprise",
            ],
            "core_report": strategy_core_report.report(),
            "scoring_report": strategy_scoring_report.report(),
            "allocation_report": strategy_allocation_report.report(),
            "simulation_report": strategy_simulation_report.report(),
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

strategy_enterprise_report_builder = StrategyEnterpriseReportBuilder()
