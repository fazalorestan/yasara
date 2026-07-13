from pydantic import BaseModel, Field

class PortablePackagePlanV1(BaseModel):
    package_name: str = "yasara_professional_portable"
    include: list[str] = Field(default_factory=list)
    exclude: list[str] = Field(default_factory=list)

class PortableBuilderV1:
    def plan(self) -> PortablePackagePlanV1:
        return PortablePackagePlanV1(
            include=["backend/**", "docs/**", "deployment/**", "windows_runtime/**", "desktop_packaging/**"],
            exclude=["backend/.venv/**", "**/__pycache__/**", "**/.pytest_cache/**", "build/**", "dist/**"],
        )
