from app.v500_alpha33_1_simple_patch_runner.service import SimplePatchRunnerFacadeV500Alpha331

def test_v500_alpha33_1_facade_contract(): assert SimplePatchRunnerFacadeV500Alpha331().contract()['manual_router_patch_required_after_this'] is False
