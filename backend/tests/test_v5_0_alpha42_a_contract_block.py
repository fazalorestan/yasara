from app.v500_alpha42_execution_core.service import ExecutionCoreFacadeV500Alpha42

def test_v500_alpha42_a_contract_block(): assert ExecutionCoreFacadeV500Alpha42().contract()['execution_allowed'] is False
