from app.platform_core.patching.planner import PatchPipelinePlanner

def test_v500_alpha21_planner():
    p=PatchPipelinePlanner().build_plan(); assert p['ready'] is True; assert p['v5_auto_discovery_enabled'] is True
