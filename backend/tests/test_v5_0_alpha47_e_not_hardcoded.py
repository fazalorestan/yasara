from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_not_hardcoded(): assert ProductionReadinessFacadeV500Alpha47().report()['hardcoded_dashboard'] is False
