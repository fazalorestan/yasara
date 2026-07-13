from pydantic import BaseModel, Field

class OwnerNoteV1(BaseModel):
    title: str
    body: str

class ReleaseOwnerNotesV1(BaseModel):
    notes: list[OwnerNoteV1] = Field(default_factory=list)

class ReleaseOwnerNotesBuilderV1:
    def build(self) -> ReleaseOwnerNotesV1:
        return ReleaseOwnerNotesV1(notes=[
            OwnerNoteV1(title="Default Safety", body="Live trading is intentionally disabled in v1.0."),
            OwnerNoteV1(title="Testing", body="Run full pytest before any delivery or archive creation."),
            OwnerNoteV1(title="Next Version", body="v1.1 should focus on production exchange connectivity behind safety gates."),
        ])
