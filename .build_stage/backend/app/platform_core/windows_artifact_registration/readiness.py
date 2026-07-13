from app.platform_core.windows_artifact_registration.report import local_exe_artifact_registration_report_service
class LocalExeArtifactRegistrationReadinessGate:
    def run(self):
        r=local_exe_artifact_registration_report_service.report()
        ready=r['ready'] and r['exe_detector']['ready'] and r['hash_generator']['requires_existing_artifact'] and r['portable_zip']['requires_hash'] and r['registry_update']['requires_manifest'] and r['smoke_result']['requires_real_exe'] and r['real_execution_enabled'] is False and r['real_broker_connection_enabled'] is False
        return {'ready':ready,'checks':{'exe_detector_ready':r['exe_detector']['ready'],'hash_required':r['hash_generator']['requires_existing_artifact'],'zip_requires_hash':r['portable_zip']['requires_hash'],'registry_requires_manifest':r['registry_update']['requires_manifest'],'smoke_requires_real_exe':r['smoke_result']['requires_real_exe'],'final_exe_generated':r['final_exe_generated'],'artifact_registered':r['artifact_registered']}}
local_exe_artifact_registration_readiness_gate=LocalExeArtifactRegistrationReadinessGate()
