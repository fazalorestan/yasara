from pydantic import BaseModel, Field

class PackageSectionV1(BaseModel):
    name: str
    include_patterns: list[str] = Field(default_factory=list)
    exclude_patterns: list[str] = Field(default_factory=list)

class FinalPackageManifestV1(BaseModel):
    package_name: str = "yasara_v1_0_professional"
    sections: list[PackageSectionV1] = Field(default_factory=list)

class FinalPackageManifestBuilderV1:
    def build(self) -> FinalPackageManifestV1:
        return FinalPackageManifestV1(sections=[
            PackageSectionV1(name="backend", include_patterns=["backend/**"], exclude_patterns=["backend/.venv/**", "**/__pycache__/**"]),
            PackageSectionV1(name="docs", include_patterns=["docs/**"]),
            PackageSectionV1(name="deployment", include_patterns=["deployment/**"]),
            PackageSectionV1(name="runtime", include_patterns=["windows_runtime/**", "desktop_packaging/**"]),
            PackageSectionV1(name="release", include_patterns=["release/**", "release_automation/**"]),
        ])
