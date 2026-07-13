from app.platform_core.state.state_store import PluginStateStore

def test_v428_state_store():
    store = PluginStateStore()
    record = store.set_state("p", {"x": 1})
    assert record.plugin == "p"
    assert store.get_state("p").state["x"] == 1
