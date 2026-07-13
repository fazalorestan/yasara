from app.v500_alpha36_plugin_versioning.service import PluginVersioningFacadeV500Alpha36

def test_v500_alpha36_c_facade_supported():
 r=PluginVersioningFacadeV500Alpha36().supported(); assert r is not None
