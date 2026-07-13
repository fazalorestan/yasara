class MarketDataQualityValidator:
    def validate_ohlcv(self, candle: dict):
        errors = []
        for key in ["symbol", "timeframe", "open_time", "open", "high", "low", "close", "volume"]:
            if key not in candle:
                errors.append(f"missing_{key}")
        if not errors:
            if float(candle["high"]) < float(candle["low"]):
                errors.append("high_less_than_low")
            if float(candle["volume"]) < 0:
                errors.append("negative_volume")
        return {"valid": len(errors) == 0, "errors": errors}

    def validate_orderbook(self, book: dict):
        errors = []
        if "symbol" not in book:
            errors.append("missing_symbol")
        if "bids" not in book:
            errors.append("missing_bids")
        if "asks" not in book:
            errors.append("missing_asks")
        for side in ["bids", "asks"]:
            for level in book.get(side, []):
                if float(level.get("price", 0)) <= 0:
                    errors.append(f"{side}_invalid_price")
                if float(level.get("quantity", 0)) < 0:
                    errors.append(f"{side}_invalid_quantity")
        return {"valid": len(errors) == 0, "errors": errors}

    def validate_trade(self, trade: dict):
        errors = []
        for key in ["symbol", "price", "quantity"]:
            if key not in trade:
                errors.append(f"missing_{key}")
        if not errors:
            if float(trade["price"]) <= 0:
                errors.append("invalid_price")
            if float(trade["quantity"]) <= 0:
                errors.append("invalid_quantity")
        return {"valid": len(errors) == 0, "errors": errors}

market_data_quality_validator = MarketDataQualityValidator()
