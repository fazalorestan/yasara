from app.dashboard_v1.engine.panel_builder import DashboardPanelBuilderV1

def test_dashboard_portfolio_panel_metrics():
    panel = DashboardPanelBuilderV1().portfolio_panel(equity=12000, exposure=3000, pnl=250)
    assert panel.panel_id == "portfolio"
    assert len(panel.metrics) == 3
    assert panel.metrics[0].value == 12000
