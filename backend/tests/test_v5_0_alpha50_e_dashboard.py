from app.platform_core.release_candidate.toggle_dashboard_contract import AutoTradingToggleDashboardContract

def test_dashboard(): assert AutoTradingToggleDashboardContract().dashboard()['default_state']=='off_signal_only'
