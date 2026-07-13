from app.platform_core.broker_layer.enterprise.report import BrokerEnterpriseReportBuilder

def test_v500_alpha37_d_report_packages(): assert len(BrokerEnterpriseReportBuilder().build()['packages']) == 4