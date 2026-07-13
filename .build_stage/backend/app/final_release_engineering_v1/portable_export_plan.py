from pydantic import BaseModel, Field

class PortableExportPlanV1(BaseModel):
    package_name: str = "YaSara_Professional_Portable_v1.0"
    include: list[str] = Field(default_factory=list)
    exclude: list[str] = Field(default_factory=list)

class PortableExportPlanBuilderV1:
    def build(self) -> PortableExportPlanV1:
        return PortableExportPlanV1(
            include=["backend/**", "docs/**", "deployment/**", "README.md", "CHANGELOG.md"],
            exclude=["backend/.venv/**", "**/__pycache__/**", "**/.pytest_cache/**", "dist/**", "build/**"],
        )
