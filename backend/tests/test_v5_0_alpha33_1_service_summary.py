from app.platform_core.simple_patch_runner.service import SimplePatchRunnerService

def test_v500_alpha33_1_service_summary(): assert SimplePatchRunnerService().summary()['ready'] is True
