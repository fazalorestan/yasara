from app.platform_core.kernel.service_registry import ServiceRegistry

def test_v422_service_registry():
    r=ServiceRegistry(); r.register_factory('x', lambda:{'ready':True}); assert r.get('x')['ready'] is True
