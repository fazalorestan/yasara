from app.v500_alpha50_packaging_enablement.service import GuardedPackagingEnablementFacadeV500Alpha50

def test_commercial_no_api_key(): assert GuardedPackagingEnablementFacadeV500Alpha50().report()['commercial_api_key_required'] is False
