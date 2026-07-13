from app.v500_alpha40_ai_core.service import AICoreFacadeV500Alpha40

def test_v500_alpha40_a_facade_prompt():
 r=AICoreFacadeV500Alpha40().prompt(); assert r is not None
