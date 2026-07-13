from app.platform_core.optimizer_pro.report import OptimizerProReportBuilder

def test_v500_alpha32_report(): assert OptimizerProReportBuilder().build([],None)['research_only'] is True