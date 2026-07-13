from app.platform_core.runtime_api_smoke.plan import RuntimeAPISmokePlan

def test_v500_alpha24_plan():
    p=RuntimeAPISmokePlan().build(); assert p['ready'] is True; assert p['critical'] >= 6
