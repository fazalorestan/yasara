from app.platform_core.ai_decision.services_package_b import AIDecisionServicesPackageB

def test_v500_alpha33_b_service_status(): assert AIDecisionServicesPackageB().status()['execution_allowed'] is False
