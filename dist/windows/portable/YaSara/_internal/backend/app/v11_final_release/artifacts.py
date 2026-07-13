from app.v11_final_release.models import FinalReleaseArtifactV11


class FinalReleaseArtifactBuilderV11:
    def build(self) -> list[FinalReleaseArtifactV11]:
        return [
            FinalReleaseArtifactV11(name="source_package", path="dist/YaSara_Professional_v1_1_Final.zip"),
            FinalReleaseArtifactV11(name="portable_package", path="dist/YaSara_Professional_v1_1_Portable.zip"),
            FinalReleaseArtifactV11(name="build_info", path="BUILD_INFO.json"),
            FinalReleaseArtifactV11(name="version_file", path="VERSION"),
            FinalReleaseArtifactV11(name="release_notes", path="RELEASE_NOTES_V1_1.md"),
            FinalReleaseArtifactV11(name="changelog", path="CHANGELOG_V1_1.md"),
            FinalReleaseArtifactV11(name="checksums", path="dist/SHA256SUMS.txt"),
        ]
