from app.v500_alpha46_workspace_navigation.models import WorkspaceNavigationSummaryV500Alpha46

def test_summary():
 s=WorkspaceNavigationSummaryV500Alpha46(); assert s.ready and s.test_pack_size==80 and s.hardcoded_dashboard is False
