from app.v500_alpha46_core_stabilization.service import CoreStabilizationFacadeV500Alpha46

def test_no_real_broker(): assert CoreStabilizationFacadeV500Alpha46().report()['real_broker_connection_enabled'] is False
