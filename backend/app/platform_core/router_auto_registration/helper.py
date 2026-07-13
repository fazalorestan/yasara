class FastAPIRouterRegistrationHelperContract:
    def contract(self):
        return {
            "ready": True,
            "strategy": "discover_import_verify_include",
            "manual_router_patch_required": False,
            "fail_fast_on_import_error": True,
            "swagger_visibility_required": True,
        }

fastapi_router_registration_helper_contract = FastAPIRouterRegistrationHelperContract()
