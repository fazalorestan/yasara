from app.v11_dashboard_runtime.panel_builder import DashboardPanelBuilderV11

def test_dashboard_panel_builder():
    panels = DashboardPanelBuilderV11().all_panels()
    keys = [panel.key for panel in panels]
    assert "market_snapshot" in keys
    assert "exchange_connectivity" in keys
    assert "ai_market_intelligence" in keys
