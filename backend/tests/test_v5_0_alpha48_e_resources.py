from app.platform_core.windows_builder.resource_manifest import WindowsResourceManifest

def test_resources():
 assert WindowsResourceManifest().manifest()['icon_required'] is True
