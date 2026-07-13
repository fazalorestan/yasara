from app.platform_core.windows_packaging_enablement.safety_report import guarded_packaging_safety_report_service
class GuardedPackagingReadinessGate:
    def run(self):
        r=guarded_packaging_safety_report_service.report()
        ready=r['ready'] and r['execute_guard']['requires_user_flag']=='--execute' and r['dependency_check']['dependencies_validated_by_contract'] and r['pyinstaller_check']['must_be_available_before_execute'] and r['real_build_gate']['can_attempt_real_build'] and r['real_build_gate']['blocks_trading_execution'] and r['real_build_gate']['blocks_broker_connection'] and r['artifact_hash_plan']['hash_required'] and r['final_exe_generated'] is False
        return {'ready':ready,'checks':{'execute_guard_ready':r['execute_guard']['ready'],'dependency_check_ready':r['dependency_check']['ready'],'pyinstaller_check_ready':r['pyinstaller_check']['ready'],'real_build_gate_ready':r['real_build_gate']['ready'],'hash_required':r['artifact_hash_plan']['hash_required'],'final_exe_generated':r['final_exe_generated']}}
guarded_packaging_readiness_gate=GuardedPackagingReadinessGate()
