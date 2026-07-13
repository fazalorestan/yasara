from enum import StrEnum
from pydantic import BaseModel

class ReleaseChannelV1(StrEnum):
    STABLE = "stable"
    BETA = "beta"
    DEV = "dev"

class ReleaseChannelStateV1(BaseModel):
    channel: ReleaseChannelV1 = ReleaseChannelV1.STABLE
    version: str = "1.0.0"

class ReleaseChannelServiceV1:
    def is_prerelease(self, state: ReleaseChannelStateV1) -> bool:
        return state.channel in {ReleaseChannelV1.BETA, ReleaseChannelV1.DEV}
