from pydantic import BaseModel

class FeatureFlagV1(BaseModel):
    key: str
    enabled: bool = False

class FeatureFlagServiceV1:
    def is_enabled(self, flags: list[FeatureFlagV1], key: str) -> bool:
        return any(flag.key == key and flag.enabled for flag in flags)
