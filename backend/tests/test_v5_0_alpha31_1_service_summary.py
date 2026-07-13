from app.platform_core.patch_orchestrator.service import PatchOrchestratorService

def test_v500_alpha31_1_service_summary(): assert PatchOrchestratorService().summary()['ready'] is True
