from app.platform_core.patch_runner_definitive.service import DefinitivePatchRunnerService

def test_v500_alpha32_1_sort_key_numeric(): assert DefinitivePatchRunnerService().version_key('apply_v5_0_32_x.py')[:3] == (5,0,32)
