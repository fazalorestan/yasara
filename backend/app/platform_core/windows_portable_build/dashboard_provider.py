from app.platform_core.windows_portable_build.internal_manifest import windows_internal_build_manifest
from app.platform_core.windows_portable_build.artifact_registration import windows_portable_artifact_registration_contract

class WindowsPortableBuildDashboardProvider:
    def dashboard(self):
        manifest = windows_internal_build_manifest.manifest()
        artifact = windows_portable_artifact_registration_contract.register()
        return {"ready": True, "build_id": manifest["build_id"], "target": manifest["target"], "artifact_name": artifact["artifact_name"], "artifact_registered": artifact["registered"], "final_exe_generated": manifest["final_exe_generated"], "source": "windows_portable_build_contract", "hardcoded_dashboard": False}

windows_portable_build_dashboard_provider = WindowsPortableBuildDashboardProvider()
