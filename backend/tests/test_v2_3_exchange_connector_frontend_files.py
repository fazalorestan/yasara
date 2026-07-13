from pathlib import Path

def test_exchange_connector_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "exchangeConnector.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "ExchangeConnectorStatus.tsx").exists()
