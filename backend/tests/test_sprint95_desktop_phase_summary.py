from app.desktop_ui_v1.phase3_summary import DesktopUIPhaseSummaryBuilderV1

def test_desktop_phase_summary_ready():
    summary = DesktopUIPhaseSummaryBuilderV1().build()
    assert summary.ready is True
    assert "chart_models" in summary.modules
