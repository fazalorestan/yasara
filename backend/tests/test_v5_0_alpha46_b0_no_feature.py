from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_no_feature(): assert CoreStabilizationFacadeV500Alpha46().contract()['adds_new_feature'] is False
