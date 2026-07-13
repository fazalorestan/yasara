from app.rc1_hardening_v1.dependency_lock import DependencyLockBuilderV1

def test_dependency_lock():
    lock = DependencyLockBuilderV1().build()
    assert any(d.name == "fastapi" for d in lock.dependencies)
