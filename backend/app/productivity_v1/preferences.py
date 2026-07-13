from pydantic import BaseModel, Field

class UserPreferencesV1(BaseModel):
    owner_id: str = "default"
    default_exchange: str = "bitunix"
    default_timeframe: str = "1h"
    dark_mode: bool = True
    extra: dict = Field(default_factory=dict)

class UserPreferencesServiceV1:
    def update(self, current: UserPreferencesV1, **changes) -> UserPreferencesV1:
        data = current.model_dump()
        data.update({k: v for k, v in changes.items() if v is not None})
        return UserPreferencesV1(**data)
