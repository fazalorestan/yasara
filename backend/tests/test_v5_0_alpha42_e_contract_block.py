from app.v500_alpha42_execution_enterprise.service import ExecutionEnterpriseFacadeV500Alpha42

def test_v500_alpha42_e_contract_block(): assert ExecutionEnterpriseFacadeV500Alpha42().contract()['execution_allowed'] is False
