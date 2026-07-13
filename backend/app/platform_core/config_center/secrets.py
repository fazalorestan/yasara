from app.platform_core.config_center.models import SecretReference

class SecretReferenceRegistry:
    def __init__(self):
        self._refs: dict[str, SecretReference] = {}

    def register(self, ref: SecretReference):
        self._refs[ref.key] = ref
        return ref

    def get_public(self):
        return {
            k: {
                "key": v.key,
                "provider": v.provider,
                "ref": v.ref,
                "exposed": False,
            }
            for k, v in self._refs.items()
        }

    def seed_defaults(self):
        if not self._refs:
            self.register(SecretReference(key="EXCHANGE_API_KEY", provider="env", ref="EXCHANGE_API_KEY"))
            self.register(SecretReference(key="LICENSE_KEY", provider="env", ref="YASARA_LICENSE_KEY"))
        return self.get_public()

secret_reference_registry = SecretReferenceRegistry()
