from app.v52_alpha_baseline_syntax_recovery.models import BaselineSyntaxRecoverySummaryV52Alpha

def test_guard():
    assert BaselineSyntaxRecoverySummaryV52Alpha().auto_trading_enabled is False
