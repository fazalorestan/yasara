from app.platform_core.live_data_pipeline.snapshot_cache import LiveDataSnapshotCache

def test_v500_alpha39_d_clear(): assert LiveDataSnapshotCache().clear()['cleared'] is True
