from app.platform_core.live_data_pipeline.normalizer import LiveDataSnapshotNormalizer

def test_v500_alpha39_a_normalize(): assert LiveDataSnapshotNormalizer().normalize({'source_id':'s','symbol':'btc/usdt','price':1})['snapshot']['symbol']=='BTCUSDT'