from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_facade_readiness():
 r=PICCoreFacadeV500Alpha44().readiness(); assert r is not None
