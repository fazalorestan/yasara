from app.platform_core.windows_packaging.app_metadata import windows_app_metadata_service
from app.platform_core.windows_packaging.dashboard_provider import windows_packaging_dashboard_provider
from app.platform_core.windows_packaging.installer_contract import windows_installer_contract
from app.platform_core.windows_packaging.output_layout import windows_build_output_layout
from app.platform_core.windows_packaging.packaging_profile import windows_packaging_profile_service
from app.platform_core.windows_packaging.portable_contract import windows_portable_app_contract
from app.platform_core.windows_packaging.readiness import windows_packaging_readiness_gate
from app.platform_core.windows_packaging.report import windows_packaging_report_service
from app.platform_core.windows_packaging.validation import windows_packaging_validation_service
from app.v500_alpha48_windows_packaging.models import WindowsPackagingSummaryV500Alpha48

class WindowsPackagingFacadeV500Alpha48:
    def summary(self): return WindowsPackagingSummaryV500Alpha48()
    def profile(self): return windows_packaging_profile_service.profile()
    def portable(self): return windows_portable_app_contract.contract()
    def installer(self): return windows_installer_contract.contract()
    def metadata(self): return windows_app_metadata_service.metadata()
    def layout(self): return windows_build_output_layout.layout()
    def validation(self): return windows_packaging_validation_service.validate()
    def dashboard(self): return windows_packaging_dashboard_provider.dashboard()
    def report(self): return windows_packaging_report_service.report()
    def readiness(self): return windows_packaging_readiness_gate.run()
    def contract(self): return {"ready": True, "windows_packaging": "package_b_contract", "build_id": "2026.48.B.001"}

windows_packaging_facade_v500_alpha48 = WindowsPackagingFacadeV500Alpha48()
