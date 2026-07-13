from app.v500_alpha21_patch_pipeline.service import PatchPipelineFacadeV500Alpha21

def test_v500_alpha21_facade_readiness(): assert PatchPipelineFacadeV500Alpha21().readiness()['ready'] is True
