from app.v11_final_release.artifacts import FinalReleaseArtifactBuilderV11
from app.v11_final_release.checks import FinalReleaseChecksV11
from app.v11_final_release.models import FinalReleaseManifestV11


class FinalReleaseManifestBuilderV11:
    def build(self) -> FinalReleaseManifestV11:
        return FinalReleaseManifestV11(
            artifacts=FinalReleaseArtifactBuilderV11().build(),
            checks=FinalReleaseChecksV11().run(),
        )
