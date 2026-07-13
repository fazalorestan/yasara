from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_facade_report():
 r=PICCoreFacadeV500Alpha44().report(); assert r is not None
