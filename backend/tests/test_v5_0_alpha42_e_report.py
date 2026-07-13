from app.platform_core.execution_engine.enterprise.report import ExecutionEnterpriseReportBuilder

def test_v500_alpha42_e_report(): assert ExecutionEnterpriseReportBuilder().build()['ready'] is True
