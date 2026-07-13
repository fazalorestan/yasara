from app.platform_core.release_registry.release_notes import ReleaseNotesRegistry

def test_notes(): assert ReleaseNotesRegistry().notes()['changelog_present'] is True
