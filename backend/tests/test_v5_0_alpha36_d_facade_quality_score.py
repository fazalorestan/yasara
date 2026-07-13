from app.v500_alpha36_plugin_enterprise.service import PluginEnterpriseFacadeV500Alpha36

def test_v500_alpha36_d_facade_quality_score():
 r=PluginEnterpriseFacadeV500Alpha36().quality_score(); assert r is not None
