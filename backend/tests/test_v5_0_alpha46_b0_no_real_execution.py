from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_no_real_execution(): assert CoreStabilizationFacadeV500Alpha46().report()['real_execution_enabled'] is False
