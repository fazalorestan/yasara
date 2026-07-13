from app.platform_core.optimizer_pro.walk_forward import WalkForwardService

def test_v500_alpha32_wf_windows(): assert WalkForwardService().windows()['count']>=3