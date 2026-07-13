from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_facade_contract():
 r=PICCoreFacadeV500Alpha44().contract(); assert r is not None
