from pydantic import BaseModel, Field

class FinalFolderV1(BaseModel):
    path: str
    purpose: str

class FinalProjectStructureV1(BaseModel):
    folders: list[FinalFolderV1] = Field(default_factory=list)

class FinalProjectStructureBuilderV1:
    def build(self) -> FinalProjectStructureV1:
        return FinalProjectStructureV1(folders=[
            FinalFolderV1(path="backend", purpose="FastAPI backend and tests"),
            FinalFolderV1(path="desktop", purpose="Flutter desktop application"),
            FinalFolderV1(path="mobile", purpose="Flutter mobile application"),
            FinalFolderV1(path="deployment", purpose="Docker and deployment files"),
            FinalFolderV1(path="installer", purpose="Windows installer and portable package tools"),
            FinalFolderV1(path="docs", purpose="Final documentation"),
            FinalFolderV1(path="scripts", purpose="Build, cleanup, release and QA scripts"),
            FinalFolderV1(path="sdk", purpose="Developer SDK scaffold"),
        ])
