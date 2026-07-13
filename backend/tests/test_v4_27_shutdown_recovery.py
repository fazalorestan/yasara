from app.platform_core.extension_host.recovery import RecoveryManager
from app.platform_core.extension_host.shutdown import SafeShutdownContract

def test_v427_shutdown_recovery():
    plan = SafeShutdownContract().plan("p")
    assert "flush_queue" in plan["steps"]
    rec = RecoveryManager().recover("p", "err")
    assert rec["final_state"] == "reported"
