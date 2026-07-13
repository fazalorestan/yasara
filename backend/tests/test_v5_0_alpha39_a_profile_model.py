from app.platform_core.live_data_pipeline.models import DataSourceProfile

def test_v500_alpha39_a_profile_model(): assert DataSourceProfile('s','Source').mode=='simulated'