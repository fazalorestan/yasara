from app.platform_core.patching.self_healing.service import SelfHealingPatchPipelineService

def test_v500_alpha25_service_verify(): assert SelfHealingPatchPipelineService().verify_sample()['ready'] is True
