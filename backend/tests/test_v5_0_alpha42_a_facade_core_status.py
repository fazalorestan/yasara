from app.v500_alpha42_execution_core.service import ExecutionCoreFacadeV500Alpha42

def test_v500_alpha42_a_facade_core_status():
 r=ExecutionCoreFacadeV500Alpha42().core_status(); assert r is not None
