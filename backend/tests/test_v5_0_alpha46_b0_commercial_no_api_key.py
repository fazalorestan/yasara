from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_commercial_no_api_key(): assert CoreStabilizationFacadeV500Alpha46().report()['commercial_api_key_required'] is False
