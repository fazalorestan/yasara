from app.platform_core.router_auto_registration.readiness import RouterAutoRegistrationReadinessGate

def test_v500_alpha30_1_readiness(): assert 'score' in RouterAutoRegistrationReadinessGate().run()
