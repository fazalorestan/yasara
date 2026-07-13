from app.platform_core.exchange_layer.orderbook import ExchangeOrderbookSnapshotService

def test_v500_alpha38_b_orderbook(): assert len(ExchangeOrderbookSnapshotService().orderbook(depth=3)['bids'])==3