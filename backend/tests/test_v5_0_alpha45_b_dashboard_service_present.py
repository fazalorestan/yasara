from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_dashboard_service_present(): assert any(s['id']=='dashboard' for s in RuntimeServicesFacadeV500Alpha45().services()['services'])
