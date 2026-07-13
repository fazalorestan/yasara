from app.platform_core.optimizer_pro.report import OptimizerProReportBuilder

def test_v500_alpha32_report_block(): assert OptimizerProReportBuilder().build([],None)['execution_allowed'] is False