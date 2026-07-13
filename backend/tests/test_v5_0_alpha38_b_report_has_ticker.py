from app.platform_core.exchange_layer.market_data_report import ExchangeMarketDataReportService

def test_v500_alpha38_b_report_has_ticker(): assert 'ticker' in ExchangeMarketDataReportService().report()
