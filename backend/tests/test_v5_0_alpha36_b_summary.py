from app.v500_alpha36_plugin_runtime_sandbox.models import PluginRuntimeSandboxSummaryV500Alpha36

def test_v500_alpha36_b_summary():
 s=PluginRuntimeSandboxSummaryV500Alpha36(); assert s.ready and s.test_pack_size==60