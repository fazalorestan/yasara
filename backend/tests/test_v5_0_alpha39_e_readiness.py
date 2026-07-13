from app.platform_core.live_data_pipeline.enterprise.readiness import LiveDataEnterpriseReadinessGate

def test_v500_alpha39_e_readiness(): assert LiveDataEnterpriseReadinessGate().run()['ready'] is True
