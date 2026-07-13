import pytest
from app.version_v1.application.service import VersionServiceV1

@pytest.mark.asyncio
async def test_stable_version_info():
    version = await VersionServiceV1().version()
    assert version.version == "1.0.0"
    assert version.channel == "stable"
    assert version.build == "stable-production"

@pytest.mark.asyncio
async def test_stable_manifest_ready_components():
    manifest = await VersionServiceV1().manifest()
    assert any(c.name == "risk_engine" for c in manifest.components)
    assert any(c.name == "strategy_builder" for c in manifest.components)
