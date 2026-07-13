from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_commercial_no_execution(): assert PICCoreFacadeV500Alpha44().version_state()['commercial_execution_engine_enabled'] is False
