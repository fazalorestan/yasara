from app.platform_core.windows_packaging_enablement.artifact_hash_plan import windows_packaging_artifact_hash_plan
from app.platform_core.windows_packaging_enablement.dependency_check import local_packaging_dependency_check
from app.platform_core.windows_packaging_enablement.execute_guard import packaging_execute_guard
from app.platform_core.windows_packaging_enablement.pyinstaller_check import pyinstaller_availability_check
from app.platform_core.windows_packaging_enablement.real_build_gate import windows_real_build_gate
class GuardedPackagingSafetyReportService:
    def report(self):
        return {'ready': True,'build_id':'2026.50.C.001','execute_guard':packaging_execute_guard.guard(),'dependency_check':local_packaging_dependency_check.check(),'pyinstaller_check':pyinstaller_availability_check.check(),'real_build_gate':windows_real_build_gate.gate(),'artifact_hash_plan':windows_packaging_artifact_hash_plan.plan(),'final_exe_generated':False,'real_execution_enabled':False,'real_broker_connection_enabled':False,'commercial_execution_engine_enabled':False,'commercial_api_key_required':False}
guarded_packaging_safety_report_service=GuardedPackagingSafetyReportService()
GuardedPackagingSafetyReport=GuardedPackagingSafetyReportService
guarded_packaging_safety_report=guarded_packaging_safety_report_service
