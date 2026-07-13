from app.platform_core.build_pipeline.profile_manager import BuildProfileManager

def test_profiles(): assert BuildProfileManager().profiles()['windows_profile_ready'] is True
