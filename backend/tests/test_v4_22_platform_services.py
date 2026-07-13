from app.platform_core.services.cache import Cache
from app.platform_core.services.queue import Queue
from app.platform_core.services.api_gateway import APIGatewayUtilities

def test_v422_platform_services():
    c=Cache(); c.set('a',1); assert c.get('a')==1
    q=Queue(); q.push('x'); assert q.pop()=='x'
    assert APIGatewayUtilities().standard_response()['ready'] is True
