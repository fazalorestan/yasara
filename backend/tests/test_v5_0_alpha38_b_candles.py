from app.platform_core.exchange_layer.candles import ExchangeCandleContractService

def test_v500_alpha38_b_candles(): assert len(ExchangeCandleContractService().candles(limit=3)['candles'])==3