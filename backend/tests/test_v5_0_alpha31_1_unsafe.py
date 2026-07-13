from app.platform_core.patch_orchestrator.service import PatchOrchestratorService

def test_v500_alpha31_1_unsafe(): assert PatchOrchestratorService().is_safe('apply_v5_wipe.py') is False
