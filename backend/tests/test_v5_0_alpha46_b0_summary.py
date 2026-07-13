from app.v500_alpha46_core_stabilization.models import CoreStabilizationSummaryV500Alpha46

def test_summary():
 s=CoreStabilizationSummaryV500Alpha46(); assert s.ready and s.stabilization_only and s.adds_new_feature is False
