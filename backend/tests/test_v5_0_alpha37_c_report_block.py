from app.platform_core.broker_layer.connectivity_report import BrokerConnectivityReportService

def test_v500_alpha37_c_report_block(): assert BrokerConnectivityReportService().report()['execution_allowed'] is False