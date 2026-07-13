from app.v11_final_release.manifest import FinalReleaseManifestBuilderV11
from app.v11_final_release.models import FinalReleaseSummaryV11


class FinalReleaseServiceV11:
    def manifest(self):
        return FinalReleaseManifestBuilderV11().build()

    def summary(self):
        manifest = self.manifest()
        checks_total = len(manifest.checks)
        checks_passed = sum(1 for check in manifest.checks if check.passed)
        return FinalReleaseSummaryV11(
            ready=checks_total > 0 and checks_passed == checks_total and manifest.live_trading_enabled is False,
            checks_passed=checks_passed,
            checks_total=checks_total,
        )

    def package_plan(self) -> dict:
        manifest = self.manifest()
        return {
            "ready": self.summary().ready,
            "version": manifest.version,
            "artifacts": [artifact.model_dump() for artifact in manifest.artifacts],
            "commands": [
                "backend\\scripts\\final_qa_v1_1.bat",
                "backend\\scripts\\build_v1_1_final_package.bat",
            ],
        }
