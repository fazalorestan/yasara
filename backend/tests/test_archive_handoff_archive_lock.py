from app.archive_handoff_v1.archive_lock import ArchiveLockBuilderV1

def test_archive_lock():
    lock = ArchiveLockBuilderV1().build()
    assert lock.locked is True
    assert lock.version == "1.0.0"
