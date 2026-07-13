from app.platform_core.patching.self_healing.service import SelfHealingPatchPipelineService

def test_v500_alpha25_service_parse(): assert SelfHealingPatchPipelineService().parse('apply_v5_0_alpha_25_x.py')['alpha'] == 25
