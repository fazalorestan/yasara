from app.platform_core.exchange_layer.ticker import ExchangeTickerSnapshotService

def test_v500_alpha38_b_ticker(): assert ExchangeTickerSnapshotService().ticker()['last_price']==50000.0