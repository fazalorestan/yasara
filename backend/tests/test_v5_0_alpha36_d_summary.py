from app.v500_alpha36_plugin_enterprise.models import PluginEnterpriseSummaryV500Alpha36

def test_v500_alpha36_d_summary():
 s=PluginEnterpriseSummaryV500Alpha36(); assert s.ready and s.test_pack_size==65
