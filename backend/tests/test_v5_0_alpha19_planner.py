from app.platform_core.api_routing.planner import RouterRegistrationPlanner

def test_v500_alpha19_planner():
    p=RouterRegistrationPlanner().build_plan(); assert 'total_modules' in p; assert p['mode']=='registration_plan_only'
