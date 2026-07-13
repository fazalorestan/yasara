from app.v500_alpha2_indicator_marketplace.service import IndicatorMarketplaceFacadeV500Alpha2

def test_v500_alpha2_facade():
    f=IndicatorMarketplaceFacadeV500Alpha2(); assert f.summary().ready is True and f.discovery()["ready"] is True
