from app.v11_distribution.models import DistributionArtifactV11, DistributionSummaryV11


class FinalDistributionServiceV11:
    def windows_outputs(self) -> list[DistributionArtifactV11]:
        return [
            DistributionArtifactV11(name="Windows Portable ZIP", target="windows", path="dist/YaSara_Professional_v1_1_Windows_Portable.zip"),
            DistributionArtifactV11(name="Windows Final ZIP", target="windows", path="dist/YaSara_Professional_v1_1_Windows_Final.zip"),
            DistributionArtifactV11(name="Windows Installer Plan", target="windows", path="dist/YaSara_Windows_Installer_Plan.txt"),
            DistributionArtifactV11(name="Windows Checksums", target="windows", path="dist/SHA256SUMS_WINDOWS.txt"),
        ]

    def mobile_outputs(self) -> list[DistributionArtifactV11]:
        return [
            DistributionArtifactV11(name="Mobile PWA ZIP", target="mobile", path="dist/YaSara_Professional_v1_1_Mobile_PWA.zip"),
            DistributionArtifactV11(name="Android Wrapper Guide", target="mobile", path="mobile_output/ANDROID_BUILD_GUIDE.md"),
            DistributionArtifactV11(name="PWA Manifest", target="mobile", path="mobile_output/manifest.webmanifest"),
            DistributionArtifactV11(name="Mobile API Config", target="mobile", path="mobile_output/mobile_api_config.json"),
            DistributionArtifactV11(name="Mobile Checksums", target="mobile", path="dist/SHA256SUMS_MOBILE.txt"),
        ]

    def summary(self) -> DistributionSummaryV11:
        return DistributionSummaryV11(
            ready=True,
            windows_outputs=self.windows_outputs(),
            mobile_outputs=self.mobile_outputs(),
        )
