from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_facade_duplicate_detector():
 r=CoreStabilizationFacadeV500Alpha46().duplicate_detector(); assert r is not None
