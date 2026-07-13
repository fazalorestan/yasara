class LocalExeSmokeResultContract:
    def result(self):
        return {'ready': True,'requires_real_exe':True,'launch_test':'pending','dashboard_test':'pending','backend_health_test':'pending','signal_only_default':True,'auto_trading_enabled':False,'smoke_passed':False}
local_exe_smoke_result_contract=LocalExeSmokeResultContract()
