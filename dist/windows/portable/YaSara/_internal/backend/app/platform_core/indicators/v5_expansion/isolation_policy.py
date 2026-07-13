class IndicatorIsolationPolicy:
    def policy(self):
        return {"ready":True,"rules":["indicator_plugins_do_not_import_each_other","indicator_runtime_is_analysis_only","execution_layer_is_not_accessible_from_indicator","chart_consumes_overlay_contract_only"],"execution_allowed":False,"mode":"policy_only"}
indicator_isolation_policy = IndicatorIsolationPolicy()
