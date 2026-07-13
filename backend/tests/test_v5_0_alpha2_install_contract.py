from app.platform_core.indicators.marketplace.install_contract import IndicatorInstallContract

def test_v500_alpha2_install_contract():
    c=IndicatorInstallContract(); assert c.install_plan("yasara")["destructive"] is False and c.enable_plan("yasara")["requires_user_confirmation"] is True
