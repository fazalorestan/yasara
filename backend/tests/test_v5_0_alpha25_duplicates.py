from app.platform_core.patching.self_healing.duplicates import PatchDuplicateDetector

def test_v500_alpha25_duplicates():
    scripts=[{'script':'a','version':{'sort_key':(5,0,1,'a')}},{'script':'b','version':{'sort_key':(5,0,1,'b')}}]; assert PatchDuplicateDetector().detect(scripts)['ready'] is False
