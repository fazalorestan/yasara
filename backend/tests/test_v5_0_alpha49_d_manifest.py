from app.platform_core.windows_portable_build.internal_manifest import WindowsInternalBuildManifest

def test_manifest(): assert WindowsInternalBuildManifest().manifest()['target']=='windows-x64-portable'
