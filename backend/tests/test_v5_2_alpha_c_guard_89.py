from app.v52_alpha_windows_spec_fix.models import WindowsSpecOutputFixSummaryV52Alpha

def test_guard(): assert WindowsSpecOutputFixSummaryV52Alpha().auto_trading_enabled is False
