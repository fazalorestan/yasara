from app.platform_core.exchanges.metadata import ExchangeMetadataRegistry
def test_v500_alpha16_metadata_iran():
    m = ExchangeMetadataRegistry().get("nobitex")
    assert m["country"] == "iran"
    assert m["rate_limit_per_minute"] == 300
