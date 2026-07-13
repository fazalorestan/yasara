from app.platform_core.patching.service import PatchPipelineService

def test_v500_alpha21_service_plan(): assert PatchPipelineService().plan()['ready'] is True
