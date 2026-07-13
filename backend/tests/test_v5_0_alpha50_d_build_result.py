from app.platform_core.windows_artifact_registration.build_result_reader import LocalBuildResultReader

def test_build_result(): assert LocalBuildResultReader().read()['build_succeeded'] is False
