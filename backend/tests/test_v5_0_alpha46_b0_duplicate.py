from app.platform_core.stabilization.duplicate_detector import DuplicateDetectorService

def test_duplicate(): assert DuplicateDetectorService().scan()['safe_to_refactor'] is True
