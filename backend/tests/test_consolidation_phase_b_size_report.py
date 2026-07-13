from app.consolidation_v1.size_report import ProjectSizeReportBuilderV1

def test_phase_b_size_report_has_removable_items():
    report = ProjectSizeReportBuilderV1().build_static_policy()
    assert len(report.removable_items) >= 1
    assert any(item.path == ".venv" for item in report.items)
