from app.platform_core.patch_runner_definitive.service import DefinitivePatchRunnerService

def test_v500_alpha32_1_safe_bad(): assert DefinitivePatchRunnerService().safe('apply_v5_wipe.py') is False
