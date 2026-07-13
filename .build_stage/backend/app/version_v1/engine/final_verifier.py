from app.version_v1.domain.models import FinalVerificationResult, ReleaseComponentStatus
from app.version_v1.engine.manifest import ReleaseManifestBuilderV1

class FinalReleaseVerifierV1:
    def verify(self, root_path: str | None = None) -> FinalVerificationResult:
        manifest = ReleaseManifestBuilderV1().build(root_path)
        blockers = []
        warnings = []
        for component in manifest.components:
            if component.status == ReleaseComponentStatus.BLOCKED:
                blockers.append(f"{component.name}: {component.notes}")
            if component.status == ReleaseComponentStatus.WARNING:
                warnings.append(f"{component.name}: {component.notes}")
        total = len(manifest.components)
        passed = len([c for c in manifest.components if c.status != ReleaseComponentStatus.BLOCKED])
        return FinalVerificationResult(
            ready=len(blockers) == 0,
            total_checks=total,
            passed_checks=passed,
            warnings=warnings,
            blockers=blockers,
            manifest=manifest,
        )
