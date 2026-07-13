from app.platform_core.patching.service import PatchPipelineService

def test_v500_alpha21_service_classify(): assert PatchPipelineService().classify('apply_v5_test.py')['family']=='v5'
