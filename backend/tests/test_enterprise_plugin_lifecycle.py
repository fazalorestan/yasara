from app.enterprise_v1.plugin_lifecycle import PluginLifecycleManagerV1, PluginLifecycleRecordV1, PluginLifecycleStateV1

def test_plugin_lifecycle_enable():
    record = PluginLifecycleManagerV1().enable(PluginLifecycleRecordV1(plugin_id="p1"))
    assert record.state == PluginLifecycleStateV1.ENABLED
