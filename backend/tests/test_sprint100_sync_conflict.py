from app.cloud_v1.sync_conflict import ConflictStrategy, SyncConflictResolverV1, SyncConflictV1

def test_sync_conflict_remote_wins():
    result = SyncConflictResolverV1().resolve(SyncConflictV1(key="x", local={"v":1}, remote={"v":2}), ConflictStrategy.REMOTE_WINS)
    assert result["v"] == 2
