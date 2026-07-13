from app.platform_core.production_runtime.lifecycle_manager import RuntimeLifecycleManager

def test_lifecycle(): assert 'startup' in RuntimeLifecycleManager().lifecycle()['allowed_transitions']
