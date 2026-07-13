from pydantic import BaseModel, Field

class FinalReleaseTreeItemV1(BaseModel):
    path: str
    required: bool = True

class FinalReleaseTreeV1(BaseModel):
    root: str = "YaSara_Professional_v1.0"
    items: list[FinalReleaseTreeItemV1] = Field(default_factory=list)

class FinalReleaseTreeBuilderV1:
    def build(self) -> FinalReleaseTreeV1:
        return FinalReleaseTreeV1(items=[
            FinalReleaseTreeItemV1(path="backend"),
            FinalReleaseTreeItemV1(path="desktop", required=False),
            FinalReleaseTreeItemV1(path="mobile", required=False),
            FinalReleaseTreeItemV1(path="deployment"),
            FinalReleaseTreeItemV1(path="installer"),
            FinalReleaseTreeItemV1(path="sdk", required=False),
            FinalReleaseTreeItemV1(path="docs"),
            FinalReleaseTreeItemV1(path="plugins", required=False),
            FinalReleaseTreeItemV1(path="examples", required=False),
            FinalReleaseTreeItemV1(path="README.md"),
            FinalReleaseTreeItemV1(path="CHANGELOG.md"),
            FinalReleaseTreeItemV1(path="LICENSE", required=False),
        ])
