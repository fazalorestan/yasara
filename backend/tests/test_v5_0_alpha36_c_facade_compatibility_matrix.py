from app.v500_alpha36_plugin_versioning.service import PluginVersioningFacadeV500Alpha36

def test_v500_alpha36_c_facade_compatibility_matrix():
 r=PluginVersioningFacadeV500Alpha36().compatibility_matrix(); assert r is not None
