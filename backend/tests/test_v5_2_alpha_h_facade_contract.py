from app.v52_alpha_fastapi_staticfiles_fix.service import FastAPIStaticFilesFixFacadeV52Alpha

def test_facade_contract(): assert FastAPIStaticFilesFixFacadeV52Alpha().contract() is not None
