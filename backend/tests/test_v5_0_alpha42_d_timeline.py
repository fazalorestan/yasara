from app.platform_core.execution_engine.execution_timeline import ExecutionTimelineService

def test_v500_alpha42_d_timeline(): assert ExecutionTimelineService().timeline()['count']==3
