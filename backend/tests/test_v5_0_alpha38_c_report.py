from app.platform_core.exchange_layer.connectivity_report import ExchangeConnectivityReportService

def test_v500_alpha38_c_report(): assert ExchangeConnectivityReportService().report()['ready'] is True