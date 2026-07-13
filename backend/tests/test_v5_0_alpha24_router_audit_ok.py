from app.platform_core.runtime_api_smoke.router_audit import RouterRegistrationAudit

def test_v500_alpha24_router_audit_ok(): assert RouterRegistrationAudit().audit()['ready'] is True
