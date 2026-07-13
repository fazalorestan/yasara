from app.platform_core.router_auto_registration.planner import RouterAutoRegistrationPlanner

def test_v500_alpha30_1_planner(): assert 'total_modules' in RouterAutoRegistrationPlanner().build_plan()
