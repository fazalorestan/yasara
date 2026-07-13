from app.platform_core.patching.self_healing.planner import SelfHealingPatchPlanner

def test_v500_alpha25_planner(): assert 'dry_run' in SelfHealingPatchPlanner().dry_run()
