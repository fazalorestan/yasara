from pydantic import BaseModel

class ExchangeConnectorSummaryV500Alpha16(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_16_exchange_connector_framework"
    scope: str = "exchange_connector_framework"
    real_exchange_connection: bool = False
    broker_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    default_exchange_count: int = 18
    backward_compatible: bool = True
    test_pack_size: int = 20
