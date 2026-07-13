from app.platform_core.broker_layer.connectivity_report import BrokerConnectivityReportService

def test_v500_alpha37_c_report(): assert BrokerConnectivityReportService().report()['ready'] is True