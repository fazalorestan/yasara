from pydantic import BaseModel, Field
from app.stable_release_v1.stable_manifest import StableReleaseManifestBuilderV1
from app.stable_release_v1.stable_validation import StableValidationBuilderV1

class StableReleaseSummaryV1(BaseModel):
    ready: bool
    release_name: str
    version: str
    total_tests_note: str = "Run full pytest before publishing."
    next_phase: str = "final_package_export"

class StableReleaseSummaryBuilderV1:
    def build(self) -> StableReleaseSummaryV1:
        manifest = StableReleaseManifestBuilderV1().build()
        validation = StableValidationBuilderV1().build()
        return StableReleaseSummaryV1(
            ready=validation.stable_ready,
            release_name=manifest.release_name,
            version=manifest.version,
        )
