from app.v500_alpha31_optimizer.service import OptimizerFacadeV500Alpha31

def test_v500_alpha31_facade_grid(): assert OptimizerFacadeV500Alpha31().grid()['total'] == 9
