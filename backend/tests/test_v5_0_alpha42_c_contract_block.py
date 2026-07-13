from app.v500_alpha42_execution_lifecycle.service import ExecutionLifecycleFacadeV500Alpha42

def test_v500_alpha42_c_contract_block(): assert ExecutionLifecycleFacadeV500Alpha42().contract()['execution_allowed'] is False
