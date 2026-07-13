from app.v11_market_data.models import RateLimitRuleV11


class ExchangeRateLimitProfileBuilderV11:
    def build(self) -> list[RateLimitRuleV11]:
        return [
            RateLimitRuleV11(exchange="binance", max_requests=1200, per_seconds=60),
            RateLimitRuleV11(exchange="bitunix", max_requests=600, per_seconds=60),
            RateLimitRuleV11(exchange="toobit", max_requests=600, per_seconds=60),
        ]
