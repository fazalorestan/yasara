from app.v500_alpha44_pic_core.service import PICCoreFacadeV500Alpha44

def test_no_real_execution(): assert PICCoreFacadeV500Alpha44().project_state()['real_execution_enabled'] is False
