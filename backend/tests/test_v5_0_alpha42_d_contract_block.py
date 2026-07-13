from app.v500_alpha42_execution_analytics.service import ExecutionAnalyticsFacadeV500Alpha42

def test_v500_alpha42_d_contract_block(): assert ExecutionAnalyticsFacadeV500Alpha42().contract()['execution_allowed'] is False
