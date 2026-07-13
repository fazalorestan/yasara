from app.final_operations_v1.troubleshooting import TroubleshootingGuideBuilderV1

def test_troubleshooting_guide():
    guide = TroubleshootingGuideBuilderV1().build()
    assert any("PYTHONPATH" in item.action for item in guide.items)
