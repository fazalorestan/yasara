from app.final_export_scripts_v1.export_summary import OneClickExportSummaryBuilderV1

def test_one_click_final_export_summary():
    summary = OneClickExportSummaryBuilderV1().build()
    assert summary.ready is True
    assert "stable.zip" in summary.archive_name
