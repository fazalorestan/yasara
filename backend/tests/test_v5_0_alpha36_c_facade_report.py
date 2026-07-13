from app.v500_alpha36_plugin_versioning.service import PluginVersioningFacadeV500Alpha36

def test_v500_alpha36_c_facade_report():
 r=PluginVersioningFacadeV500Alpha36().report(); assert r is not None
