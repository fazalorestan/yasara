from app.v52_alpha_force_merge_k_sqlalchemy_gate.models import ForceMergeKSQLAlchemyGateSummaryV52Alpha

def test_summary():
 s=ForceMergeKSQLAlchemyGateSummaryV52Alpha(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.52.L.001'
