from pathlib import Path
from app.v11_operations.models import ReleaseVerificationV11


class ReleaseVerifierV11:
    def __init__(self, root: Path | None = None):
        self.root = root or Path(__file__).resolve().parents[3]

    def required_files(self) -> list[str]:
        return [
            "windows_runtime/YaSara_Start_Backend.bat",
            "windows_runtime/YaSara_Run_Tests.bat",
            "windows_runtime/README_WINDOWS_11_INSTALL.md",
            "desktop_packaging/build_desktop_portable.ps1",
            "desktop_packaging/build_windows_installer.ps1",
            "desktop_packaging/yasara_desktop_installer.iss",
            "release_automation/qa_windows_install.ps1",
            "release_automation/create_release_bundle.ps1",
            "release_automation/generate_checksums.ps1",
            "FINAL_VERSION_FREEZE_MANIFEST.json",
            "YASARA_V1_FINAL_README.md",
            "YASARA_V1_TO_V1_1_ROADMAP.md",
        ]

    def verify(self) -> ReleaseVerificationV11:
        required = self.required_files()
        missing = [rel for rel in required if not (self.root / rel).exists()]
        return ReleaseVerificationV11(
            ready=not missing,
            required_files=required,
            missing_files=missing,
        )
