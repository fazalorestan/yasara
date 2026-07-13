from app.v500_alpha31_optimizer.service import OptimizerFacadeV500Alpha31

def test_v500_alpha31_facade_config(): assert OptimizerFacadeV500Alpha31().config()['ready'] is True
