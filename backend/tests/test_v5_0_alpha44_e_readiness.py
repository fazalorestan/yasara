from app.platform_core.project_intelligence.pic_enterprise_readiness import PICEnterpriseReadinessGate

def test_readiness(): assert PICEnterpriseReadinessGate().run()['ready'] is True
