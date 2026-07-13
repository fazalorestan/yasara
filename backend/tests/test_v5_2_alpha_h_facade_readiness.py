from app.v52_alpha_fastapi_staticfiles_fix.service import FastAPIStaticFilesFixFacadeV52Alpha

def test_facade_readiness(): assert FastAPIStaticFilesFixFacadeV52Alpha().readiness() is not None
