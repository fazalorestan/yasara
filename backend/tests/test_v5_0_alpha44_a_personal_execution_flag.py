from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_personal_execution_flag(): assert PICCoreFacadeV500Alpha44().version_state()['personal_execution_engine_enabled'] is True
