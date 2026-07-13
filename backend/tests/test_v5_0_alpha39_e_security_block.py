from app.platform_core.live_data_pipeline.enterprise.security import LiveDataEnterpriseSecurityGate

def test_v500_alpha39_e_security_block(): assert LiveDataEnterpriseSecurityGate().evaluate()['execution_allowed'] is False
