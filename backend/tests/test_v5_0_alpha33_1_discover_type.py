from app.platform_core.simple_patch_runner.service import SimplePatchRunnerService

def test_v500_alpha33_1_discover_type(): assert isinstance(SimplePatchRunnerService().discover_names('.'), list)
