from app.platform_core.auto_router_registry.audit import AutoRouterRegistryAudit

def test_v500_alpha34_0_audit_bad(): assert AutoRouterRegistryAudit().summarize({'failed_count':1})['ready'] is False