from app.platform_core.execution_engine.execution_state_machine import ExecutionStateMachine

def test_v500_alpha42_c_state(): assert ExecutionStateMachine().initial()['state']=='created'
