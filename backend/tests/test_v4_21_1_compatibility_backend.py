from app.v4211_frontend_compatibility.models import FrontendCompatibilitySummaryV4211

def test_v4211_compatibility_backend():
    s = FrontendCompatibilitySummaryV4211()
    assert s.ready is True
    assert s.preserves_v420_ui is True
    assert "WorkspaceButton" in s.compatibility_tokens
