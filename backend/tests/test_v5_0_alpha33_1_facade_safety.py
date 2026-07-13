from app.v500_alpha33_1_simple_patch_runner.service import SimplePatchRunnerFacadeV500Alpha331

def test_v500_alpha33_1_facade_safety(): assert SimplePatchRunnerFacadeV500Alpha331().safety()['safe'] is True
