from app.v500_alpha42_execution_core.service import ExecutionCoreFacadeV500Alpha42

def test_v500_alpha42_a_facade_order_intent():
 r=ExecutionCoreFacadeV500Alpha42().order_intent(); assert r is not None
