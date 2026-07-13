from app.v52_alpha_fastapi_staticfiles_fix.service import FastAPIStaticFilesFixFacadeV52Alpha

def test_facade_report(): assert FastAPIStaticFilesFixFacadeV52Alpha().report() is not None
