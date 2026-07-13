from app.platform_core.optimizer_pro.walk_forward import WalkForwardService

def test_v500_alpha32_wf_small(): assert WalkForwardService().windows(10,20,5)['count']==0