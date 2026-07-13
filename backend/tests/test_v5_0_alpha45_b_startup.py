from app.platform_core.production_runtime.startup_order import RuntimeStartupOrderPlanner

def test_startup(): assert 'execution' not in RuntimeStartupOrderPlanner().plan()['commercial_startup_order']
