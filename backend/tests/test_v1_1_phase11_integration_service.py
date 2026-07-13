from app.v11_release_candidate.integration_service import V11IntegrationService

def test_v11_integration_service_report():
    report = V11IntegrationService().report()
    assert report.ready is True
    assert len(report.modules) >= 10
    assert all(module.ready for module in report.modules)
