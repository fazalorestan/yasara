from app.platform_core.live_data_pipeline.ingestion_contract import LiveDataIngestionContract

def test_v500_alpha39_a_ingestion(): assert LiveDataIngestionContract().contract()['real_live_connection'] is False