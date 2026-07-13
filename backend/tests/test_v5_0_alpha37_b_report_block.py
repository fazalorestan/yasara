from app.platform_core.broker_layer.account_report import BrokerAccountReportService

def test_v500_alpha37_b_report_block(): assert BrokerAccountReportService().report()['execution_allowed'] is False