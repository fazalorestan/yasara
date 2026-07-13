from app.v500_alpha50_packaging_enablement.service import GuardedPackagingEnablementFacadeV500Alpha50

def test_no_real_broker(): assert GuardedPackagingEnablementFacadeV500Alpha50().report()['real_broker_connection_enabled'] is False
