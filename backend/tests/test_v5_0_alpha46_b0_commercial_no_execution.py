from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_commercial_no_execution(): assert CoreStabilizationFacadeV500Alpha46().report()['commercial_execution_engine_enabled'] is False
