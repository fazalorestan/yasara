from app.platform_core.licensing.readiness.checklist import LicenseSecurityChecklist
def test_v500_alpha14_checklist_auto_trade_block():
    r = LicenseSecurityChecklist().checklist()
    names = [i["name"] for i in r["items"]]
    assert "auto_trading_blocked_by_default" in names
