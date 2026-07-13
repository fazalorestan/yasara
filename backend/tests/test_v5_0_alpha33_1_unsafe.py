from app.platform_core.simple_patch_runner.service import SimplePatchRunnerService

def test_v500_alpha33_1_unsafe(): assert SimplePatchRunnerService().safe('apply_v5_wipe.py') is False
