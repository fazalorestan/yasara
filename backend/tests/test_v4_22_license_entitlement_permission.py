from app.platform_core.governance.license_manager import License, LicenseManager
from app.platform_core.governance.entitlements import EntitlementManager
from app.platform_core.governance.permissions import PermissionManager

def test_v422_license_entitlement_permission():
    lm=LicenseManager(); lm.register(License(key='k', entitlements=['advanced_ai'])); assert lm.validate('k') is True
    em=EntitlementManager(); em.require('advanced_ai',['advanced_ai']); assert em.allowed('advanced_ai',['advanced_ai']) is True
    pm=PermissionManager(); pm.grant('admin','execution:paper'); assert pm.has_permission('admin','execution:paper') is True
