from app.platform_core.stabilization.patch_consolidation import PatchConsolidationService

def test_patch(): assert PatchConsolidationService().summary()['backward_compatible'] is True
