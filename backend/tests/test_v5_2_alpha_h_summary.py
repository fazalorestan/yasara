from app.v52_alpha_fastapi_staticfiles_fix.models import FastAPIStaticFilesFixSummaryV52Alpha

def test_summary():
 s=FastAPIStaticFilesFixSummaryV52Alpha(); assert s.ready and s.test_pack_size==90 and s.fixed_import=='fastapi.staticfiles'
