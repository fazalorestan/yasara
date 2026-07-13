from pydantic import BaseModel, Field

class SourceBundlePlanV1(BaseModel):
    bundle_name: str = "yasara_professional_v1_0_source"
    include: list[str] = Field(default_factory=list)
    exclude: list[str] = Field(default_factory=list)

class SourceBundlePlanBuilderV1:
    def build(self) -> SourceBundlePlanV1:
        return SourceBundlePlanV1(
            include=["backend/app/**", "backend/tests/**", "backend/requirements.txt", "docs/**"],
            exclude=["backend/.venv/**", "**/__pycache__/**", "**/.pytest_cache/**", "**/*.pyc"],
        )
