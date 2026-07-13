from app.platform_core.indicators.scanner.ranking import IndicatorRankingService

def test_v446_ranking():
    r = IndicatorRankingService()
    assert r.grade(86) == "A+"
    ranked = r.rank([{"score": 10}, {"score": 90}])
    assert ranked[0]["score"] == 90
