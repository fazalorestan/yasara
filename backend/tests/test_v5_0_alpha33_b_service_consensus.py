from app.platform_core.ai_decision.services_package_b import AIDecisionServicesPackageB

def test_v500_alpha33_b_service_consensus(): assert AIDecisionServicesPackageB().consensus()['ready'] is True
