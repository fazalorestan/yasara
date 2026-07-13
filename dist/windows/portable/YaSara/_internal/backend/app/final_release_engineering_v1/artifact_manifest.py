from pydantic import BaseModel, Field

class ReleaseArtifactItemV1(BaseModel):
    name: str
    path: str
    required: bool = True
    artifact_type: str = "file"

class ArtifactManifestV1(BaseModel):
    release_name: str = "YaSara Professional v1.0"
    artifacts: list[ReleaseArtifactItemV1] = Field(default_factory=list)

class ArtifactManifestBuilderV1:
    def build(self) -> ArtifactManifestV1:
        return ArtifactManifestV1(artifacts=[
            ReleaseArtifactItemV1(name="backend_source", path="backend", artifact_type="folder"),
            ReleaseArtifactItemV1(name="documentation", path="docs", artifact_type="folder"),
            ReleaseArtifactItemV1(name="portable_package", path="dist/yasara_portable.zip", required=False),
            ReleaseArtifactItemV1(name="windows_installer", path="dist/YaSara_Setup.exe", required=False),
            ReleaseArtifactItemV1(name="docker_compose", path="deployment/docker-compose.yml", required=False),
        ])
