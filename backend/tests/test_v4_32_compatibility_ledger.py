from app.platform_core.version_migration.compatibility_ledger import BackwardCompatibilityLedger

def test_v432_compatibility_ledger():
    l = BackwardCompatibilityLedger()
    entries = l.seed_current()
    assert entries
    assert all(e["compatible"] for e in entries)
