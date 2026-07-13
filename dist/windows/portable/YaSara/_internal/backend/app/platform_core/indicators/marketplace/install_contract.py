class IndicatorInstallContract:
    def install_plan(self, indicator: str):
        return {"ready":True,"indicator":indicator,"steps":["validate_manifest","check_trust_level","check_compatibility","register_plugin","keep_disabled_until_user_enables"],"destructive":False,"execution_allowed":False,"mode":"contract_only"}
    def enable_plan(self, indicator: str): return {"ready":True,"indicator":indicator,"action":"enable","requires_user_confirmation":True,"execution_allowed":False}
    def disable_plan(self, indicator: str): return {"ready":True,"indicator":indicator,"action":"disable","safe":True,"execution_allowed":False}
indicator_install_contract = IndicatorInstallContract()
