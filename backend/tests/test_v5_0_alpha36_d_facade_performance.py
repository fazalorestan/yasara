from app.v500_alpha36_plugin_enterprise.service import PluginEnterpriseFacadeV500Alpha36

def test_v500_alpha36_d_facade_performance():
 r=PluginEnterpriseFacadeV500Alpha36().performance(); assert r is not None
