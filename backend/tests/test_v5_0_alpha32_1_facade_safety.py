from app.v500_alpha32_1_definitive_patch_runner.service import DefinitivePatchRunnerFacadeV500Alpha321

def test_v500_alpha32_1_facade_safety(): assert DefinitivePatchRunnerFacadeV500Alpha321().safety()['safe'] is True
