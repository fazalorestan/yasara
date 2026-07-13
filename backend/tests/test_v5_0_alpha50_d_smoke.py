from app.platform_core.windows_artifact_registration.smoke_result_contract import LocalExeSmokeResultContract

def test_smoke(): assert LocalExeSmokeResultContract().result()['requires_real_exe'] is True
