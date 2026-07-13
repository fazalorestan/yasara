from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_facade_health_state():
 r=PICCoreFacadeV500Alpha44().health_state(); assert r is not None
