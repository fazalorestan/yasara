from app.v11_exchange_connectivity.models import ExchangeEndpointProfileV11


class ExchangeProfileRegistryV11:
    def list_profiles(self) -> list[ExchangeEndpointProfileV11]:
        return [
            ExchangeEndpointProfileV11(
                exchange="binance",
                base_url="https://api.binance.com",
                ws_url="wss://stream.binance.com:9443/ws",
            ),
            ExchangeEndpointProfileV11(
                exchange="bitunix",
                base_url="https://fapi.bitunix.com",
                ws_url="wss://fapi.bitunix.com/public",
            ),
            ExchangeEndpointProfileV11(
                exchange="toobit",
                base_url="https://api.toobit.com",
                ws_url="wss://stream.toobit.com",
            ),
        ]

    def get(self, exchange: str) -> ExchangeEndpointProfileV11 | None:
        key = exchange.lower()
        for profile in self.list_profiles():
            if profile.exchange == key:
                return profile
        return None

    def enabled_exchange_ids(self) -> list[str]:
        return [p.exchange for p in self.list_profiles() if p.enabled]
