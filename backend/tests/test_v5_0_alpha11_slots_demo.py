from app.platform_core.licensing.activation.slots import ActivationSlotPolicy
def test_v500_alpha11_slots_demo():
    p = ActivationSlotPolicy()
    assert p.allowed_slots("demo") == 1
    assert p.can_activate("demo", 0) is True
    assert p.can_activate("demo", 1) is False
