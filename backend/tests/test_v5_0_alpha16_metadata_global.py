from app.platform_core.exchanges.metadata import ExchangeMetadataRegistry
def test_v500_alpha16_metadata_global():
    m = ExchangeMetadataRegistry().get("binance")
    assert m["country"] == "global"
    assert m["base_url"].startswith("https://")
