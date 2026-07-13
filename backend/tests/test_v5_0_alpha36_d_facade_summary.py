from app.v500_alpha36_plugin_enterprise.service import PluginEnterpriseFacadeV500Alpha36

def test_v500_alpha36_d_facade_summary():
 r=PluginEnterpriseFacadeV500Alpha36().summary(); assert r is not None
