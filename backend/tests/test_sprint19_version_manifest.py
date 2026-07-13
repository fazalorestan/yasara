import pytest
from app.version_v1.application.service import VersionServiceV1

@pytest.mark.asyncio
async def test_version_info_rc1():
    version = await VersionServiceV1().version()
    assert version.version == "1.0.0"
    assert version.channel == "stable"

@pytest.mark.asyncio
async def test_manifest_contains_backend_component():
    manifest = await VersionServiceV1().manifest()
    assert any(c.name == "backend" for c in manifest.components)
