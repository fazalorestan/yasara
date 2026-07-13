from app.platform_core.live_data_pipeline.enterprise.service import LiveDataEnterpriseService

def test_v500_alpha39_e_service_security():
 r=LiveDataEnterpriseService().security(); assert r is not None
