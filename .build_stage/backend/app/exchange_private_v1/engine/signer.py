import hashlib
import hmac
from urllib.parse import urlencode

class BinanceRequestSignerV1:
    def sign(self, params: dict, api_secret: str) -> dict:
        query = urlencode(params, doseq=True)
        signature = hmac.new(api_secret.encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
        signed = dict(params)
        signed["signature"] = signature
        return signed
