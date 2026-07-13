class ActivationSlotPolicy:
    def allowed_slots(self, license_type: str):
        return {
            "demo": 1,
            "personal": 1,
            "pro": 2,
            "elite": 3,
            "enterprise": 10,
            "lifetime": 3,
            "internal": 99,
        }.get(license_type, 0)

    def can_activate(self, license_type: str, current_activations: int):
        return current_activations < self.allowed_slots(license_type)

activation_slot_policy = ActivationSlotPolicy()
