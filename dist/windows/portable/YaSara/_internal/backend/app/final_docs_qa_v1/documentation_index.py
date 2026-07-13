from pydantic import BaseModel, Field

class DocumentationEntryV1(BaseModel):
    path: str
    title: str
    audience: str = "all"
    required: bool = True

class DocumentationIndexV1(BaseModel):
    entries: list[DocumentationEntryV1] = Field(default_factory=list)

class DocumentationIndexBuilderV1:
    def build(self) -> DocumentationIndexV1:
        return DocumentationIndexV1(entries=[
            DocumentationEntryV1(path="README.md", title="Project Overview"),
            DocumentationEntryV1(path="docs/INSTALLATION.md", title="Installation Guide", audience="user"),
            DocumentationEntryV1(path="docs/USER_GUIDE.md", title="User Guide", audience="user"),
            DocumentationEntryV1(path="docs/DEVELOPER_GUIDE.md", title="Developer Guide", audience="developer"),
            DocumentationEntryV1(path="docs/API_REFERENCE.md", title="API Reference", audience="developer"),
            DocumentationEntryV1(path="docs/SECURITY.md", title="Security Guide", audience="admin"),
            DocumentationEntryV1(path="docs/RELEASE_NOTES.md", title="Release Notes"),
        ])
