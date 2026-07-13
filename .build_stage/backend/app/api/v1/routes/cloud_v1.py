from fastapi import APIRouter
from app.cloud_v1.auth import AuthServiceV1, UserAccountV1
from app.cloud_v1.release_channel import ReleaseChannelServiceV1, ReleaseChannelStateV1

router = APIRouter(prefix="/cloud-v1", tags=["cloud-v1"])

@router.post("/session")
async def session(user: UserAccountV1):
    return AuthServiceV1().create_session(user)

@router.post("/release/is-prerelease")
async def is_prerelease(state: ReleaseChannelStateV1):
    return {"prerelease": ReleaseChannelServiceV1().is_prerelease(state)}
