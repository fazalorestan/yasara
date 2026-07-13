from app.platform_core.exchange_layer.market_metadata import ExchangeMarketMetadataService

def test_v500_alpha38_b_metadata(): assert ExchangeMarketMetadataService().metadata()['quote_asset']=='USDT'