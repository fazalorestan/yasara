from pydantic import BaseModel
class ObservabilitySummaryV434(BaseModel):
 ready:bool=True
 no_new_trading_features:bool=True
 backward_compatible:bool=True
 live_execution_enabled:bool=False
