from app.platform_core.router_auto_registration.service import RouterAutoRegistrationService

def test_v500_alpha30_1_service_audit(): assert RouterAutoRegistrationService().audit_sample()['ready'] is True
