import pytest
from app.v11_exchange_connectivity.rest_client import ExchangeRestClientV11

def test_rest_client_read_only_request():
    client = ExchangeRestClientV11()
    request = client.build_request("binance", "/api/v3/ticker/price")
    assert request.read_only is True
    assert request.path.startswith("https://api.binance.com")

def test_rest_client_blocks_signed():
    client = ExchangeRestClientV11()
    with pytest.raises(ValueError):
        client.build_request("binance", "/api/v3/order", signed=True)
