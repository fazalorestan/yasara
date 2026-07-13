from app.platform_core.release_candidate.rc_manifest import InternalRCManifest

def test_manifest(): assert InternalRCManifest().manifest()['signal_only_default'] is True
