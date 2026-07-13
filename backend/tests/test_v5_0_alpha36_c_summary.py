from app.v500_alpha36_plugin_versioning.models import PluginVersioningSummaryV500Alpha36

def test_v500_alpha36_c_summary():
 s=PluginVersioningSummaryV500Alpha36(); assert s.ready and s.test_pack_size==60