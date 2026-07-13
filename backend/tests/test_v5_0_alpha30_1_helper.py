from app.platform_core.router_auto_registration.helper import FastAPIRouterRegistrationHelperContract

def test_v500_alpha30_1_helper(): assert FastAPIRouterRegistrationHelperContract().contract()['manual_router_patch_required'] is False
