from app.v52_alpha_windows_spec_fix.models import WindowsSpecOutputFixSummaryV52Alpha

def test_summary():
 s=WindowsSpecOutputFixSummaryV52Alpha(); assert s.ready and s.test_pack_size==90 and s.standard_output.endswith('YaSara.exe')
