from app.platform_core.live_data_pipeline.models import DataSnapshot

def test_v500_alpha39_a_snapshot_model(): assert DataSnapshot('s','BTCUSDT',1).price==1