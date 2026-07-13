from app.platform_core.runtime_api_smoke.router_audit import RouterRegistrationAudit

def test_v500_alpha24_router_audit_missing(): assert RouterRegistrationAudit().audit(registered_paths=[])['ready'] is False
