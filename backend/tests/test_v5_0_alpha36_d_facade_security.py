from app.v500_alpha36_plugin_enterprise.service import PluginEnterpriseFacadeV500Alpha36

def test_v500_alpha36_d_facade_security():
 r=PluginEnterpriseFacadeV500Alpha36().security(); assert r is not None
