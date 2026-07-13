from app.platform_core.strategy_engine.enterprise.report import StrategyEnterpriseReportBuilder

def test_v500_alpha41_e_report_packages(): assert len(StrategyEnterpriseReportBuilder().build()['packages']) == 5
