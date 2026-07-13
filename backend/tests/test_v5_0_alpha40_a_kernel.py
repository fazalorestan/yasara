from app.platform_core.ai_intelligence.kernel import AIKernelService

def test_v500_alpha40_a_kernel(): assert AIKernelService().kernel_status()['memory_owned_by_yasara'] is True
