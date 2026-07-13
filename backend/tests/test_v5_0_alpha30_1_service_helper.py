from app.platform_core.router_auto_registration.service import RouterAutoRegistrationService

def test_v500_alpha30_1_service_helper(): assert RouterAutoRegistrationService().helper()['ready'] is True
