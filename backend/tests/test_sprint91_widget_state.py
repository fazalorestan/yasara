from app.desktop_ui_v1.widget_state import WidgetStateStoreV1, WidgetStateV1

def test_widget_state_store():
    store = WidgetStateStoreV1()
    store.save(WidgetStateV1(widget_id="chart", collapsed=True))
    assert store.get("chart").collapsed is True
