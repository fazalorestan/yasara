from app.v500_alpha31_optimizer.service import OptimizerFacadeV500Alpha31

def test_v500_alpha31_facade_contract(): assert OptimizerFacadeV500Alpha31().contract()['execution_allowed'] is False
