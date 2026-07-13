from app.platform_core.licensing.activation.slots import ActivationSlotPolicy
def test_v500_alpha11_slots_enterprise():
    assert ActivationSlotPolicy().allowed_slots("enterprise") == 10
