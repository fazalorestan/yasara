from datetime import datetime, timezone

def ms_to_dt(value) -> datetime:
    number = float(value)
    if number > 10_000_000_000:
        number = number / 1000
    return datetime.fromtimestamp(number, tz=timezone.utc)

def to_float(value, default: float = 0.0) -> float:
    try:
        return default if value in (None, "") else float(value)
    except (TypeError, ValueError):
        return default

def to_int(value, default: int = 0) -> int:
    try:
        return default if value in (None, "") else int(float(value))
    except (TypeError, ValueError):
        return default

def compact_symbol(symbol: str) -> str:
    return symbol.upper().replace("/", "").replace("-", "").strip()

def slash_symbol(symbol: str) -> str:
    value = compact_symbol(symbol)
    if value.endswith("USDT"):
        return f"{value[:-4]}/USDT"
    return value
