from app.v500_alpha50_packaging_enablement.service import GuardedPackagingEnablementFacadeV500Alpha50

def test_no_real_execution(): assert GuardedPackagingEnablementFacadeV500Alpha50().report()['real_execution_enabled'] is False
