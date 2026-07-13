from app.platform_core.indicators.models import ChartOverlayContract

class YaSaraIndicatorContract:
    def overlay_contract(self):
        return ChartOverlayContract(
            indicator="yasara",
            overlays=["EMA21","EMA55","EMA200","SMA7","SMA26","SMA99","DynamicSL","Entry","TP1","TP2","FibonacciLevels"],
            signals=["LONG","SHORT","BOS","CHOCH","FVG","LIQ","WHALE","DIV","RS_VS_BTC"],
            panels=["AI Decision","Risk Panel","Engine Scores","Status Bar"],
        ).__dict__

yasara_indicator_contract = YaSaraIndicatorContract()
