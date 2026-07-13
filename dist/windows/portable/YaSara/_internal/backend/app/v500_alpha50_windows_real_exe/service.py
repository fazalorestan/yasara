from app.platform_core.windows_real_exe.artifact_hash import windows_exe_artifact_hash_contract
from app.platform_core.windows_real_exe.build_script import windows_real_exe_build_script_contract
from app.platform_core.windows_real_exe.portable_builder import windows_real_portable_builder
from app.platform_core.windows_real_exe.pyinstaller_contract import windows_pyinstaller_contract
from app.platform_core.windows_real_exe.readiness import windows_real_exe_build_pipeline_readiness_gate
from app.platform_core.windows_real_exe.report import windows_real_exe_build_pipeline_report_service
from app.platform_core.windows_real_exe.smoke_test import windows_real_exe_smoke_test_contract
from app.platform_core.windows_real_exe.spec_contract import windows_exe_spec_contract
from app.v500_alpha50_windows_real_exe.models import WindowsRealExeBuildPipelineSummaryV500Alpha50

class WindowsRealExeBuildPipelineFacadeV500Alpha50:
    def summary(self): return WindowsRealExeBuildPipelineSummaryV500Alpha50()
    def pyinstaller(self): return windows_pyinstaller_contract.contract()
    def spec(self): return windows_exe_spec_contract.spec()
    def portable_builder(self): return windows_real_portable_builder.builder()
    def build_script(self): return windows_real_exe_build_script_contract.contract()
    def artifact_hash(self): return windows_exe_artifact_hash_contract.hash_contract()
    def smoke_test(self): return windows_real_exe_smoke_test_contract.smoke()
    def report(self): return windows_real_exe_build_pipeline_report_service.report()
    def readiness(self): return windows_real_exe_build_pipeline_readiness_gate.run()
    def contract(self): return {"ready": True, "windows_real_exe": "package_a_pipeline", "build_id": "2026.50.A.001"}
windows_real_exe_build_pipeline_facade_v500_alpha50 = WindowsRealExeBuildPipelineFacadeV500Alpha50()
