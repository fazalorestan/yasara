from app.platform_core.force_merge_k_sqlalchemy_gate.report import ForceMergeKSQLAlchemyGateReportService

def test_report(): assert ForceMergeKSQLAlchemyGateReportService().report()['force_merge_k'] is True
