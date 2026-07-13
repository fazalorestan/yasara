from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_facade_report():
 r=CoreStabilizationFacadeV500Alpha46().report(); assert r is not None
