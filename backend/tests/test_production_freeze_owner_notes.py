from app.production_freeze_v1.owner_notes import ReleaseOwnerNotesBuilderV1

def test_owner_notes():
    notes = ReleaseOwnerNotesBuilderV1().build()
    assert any("Live trading" in n.body for n in notes.notes)
