from app.v500_alpha36_plugin_versioning.service import PluginVersioningFacadeV500Alpha36

def test_v500_alpha36_c_facade_upgrade_plan():
 r=PluginVersioningFacadeV500Alpha36().upgrade_plan(); assert r is not None
