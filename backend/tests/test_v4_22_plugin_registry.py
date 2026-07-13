from app.platform_core.kernel.plugin_registry import PluginManifest, PluginRegistry

def test_v422_plugin_registry():
    r=PluginRegistry(); r.register(PluginManifest(name='p')); r.set_state('p','validated'); assert r.get('p')['state']=='validated'
