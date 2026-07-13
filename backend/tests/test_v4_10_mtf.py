from app.v410_market_structure_sprint2.detectors import mtf_context

def test_v410_mtf():
    m=mtf_context([{'strength':{'bias':'bullish'}},{'strength':{'bias':'bullish'}},{'strength':{'bias':'neutral'}}]); assert m['bias']=='bullish'
