from app.final_release_v1.release_notes import FinalReleaseNotesBuilderV1

def test_final_release_notes():
    notes = FinalReleaseNotesBuilderV1().build()
    assert notes.version == "1.0.0"
    assert any(section.title == "AI" for section in notes.sections)
