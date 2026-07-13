from pydantic import BaseModel, Field

class FinalDocTargetV1(BaseModel):
    filename: str
    title: str
    required: bool = True

class FinalDocsMapV1(BaseModel):
    docs: list[FinalDocTargetV1] = Field(default_factory=list)

class FinalDocsMapBuilderV1:
    def build(self) -> FinalDocsMapV1:
        return FinalDocsMapV1(docs=[
            FinalDocTargetV1(filename="README.md", title="YaSara Professional Overview"),
            FinalDocTargetV1(filename="docs/INSTALLATION.md", title="Installation Guide"),
            FinalDocTargetV1(filename="docs/USER_GUIDE.md", title="User Guide"),
            FinalDocTargetV1(filename="docs/DEVELOPER_GUIDE.md", title="Developer Guide"),
            FinalDocTargetV1(filename="docs/API_REFERENCE.md", title="API Reference"),
            FinalDocTargetV1(filename="docs/SECURITY.md", title="Security Guide"),
            FinalDocTargetV1(filename="docs/RELEASE_NOTES.md", title="Release Notes"),
        ])
