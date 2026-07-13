from pydantic import BaseModel, Field

class DocsBundlePlanV1(BaseModel):
    bundle_name: str = "yasara_professional_v1_0_docs"
    docs: list[str] = Field(default_factory=list)

class DocsBundlePlanBuilderV1:
    def build(self) -> DocsBundlePlanV1:
        return DocsBundlePlanV1(docs=[
            "README.md",
            "docs/INSTALLATION.md",
            "docs/USER_GUIDE.md",
            "docs/DEVELOPER_GUIDE.md",
            "docs/API_REFERENCE.md",
            "docs/SECURITY.md",
            "docs/RELEASE_NOTES.md",
        ])
