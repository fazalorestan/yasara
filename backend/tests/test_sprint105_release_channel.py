from app.cloud_v1.release_channel import ReleaseChannelServiceV1, ReleaseChannelStateV1, ReleaseChannelV1

def test_release_channel_prerelease():
    assert ReleaseChannelServiceV1().is_prerelease(ReleaseChannelStateV1(channel=ReleaseChannelV1.BETA)) is True
