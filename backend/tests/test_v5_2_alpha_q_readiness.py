from app.platform_core.baseline_syntax_recovery.readiness import BaselineSyntaxRecoveryReadinessGate

def test_readiness():
    assert BaselineSyntaxRecoveryReadinessGate().run()["ready"] is True
