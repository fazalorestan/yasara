from pathlib import Path

def test_v422_documentation():
    root=Path(__file__).resolve().parents[2]; docs=root/'docs'/'v4_22'
    for f in ['PLATFORM_ARCHITECTURE.md','PLUGIN_STANDARD.md','EVENT_FLOW.md','GOVERNANCE.md','EXTENSION_GUIDE.md','DEVELOPER_GUIDE.md']:
        assert (docs/f).exists()
