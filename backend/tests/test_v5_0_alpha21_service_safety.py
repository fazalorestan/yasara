from app.platform_core.patching.service import PatchPipelineService

def test_v500_alpha21_service_safety(): assert PatchPipelineService().safety('apply_v5_test.py')['allowed'] is True
