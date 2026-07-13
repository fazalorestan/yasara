from app.platform_core.indicators.pine_source.archive import PineSourceArchive

def test_v444_archive():
    a = PineSourceArchive()
    records = a.seed_defaults()
    assert "yasara:v1.0" in records
