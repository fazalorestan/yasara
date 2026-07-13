from app.v500_alpha40_ai_core.service import AICoreFacadeV500Alpha40

def test_v500_alpha40_a_facade_kernel():
 r=AICoreFacadeV500Alpha40().kernel(); assert r is not None
