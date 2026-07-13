from app.platform_core.patch_runner_definitive.service import DefinitivePatchRunnerService

def test_v500_alpha32_1_service_summary(): assert DefinitivePatchRunnerService().summary()['ready'] is True
