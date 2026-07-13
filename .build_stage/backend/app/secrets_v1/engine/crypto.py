import base64
import hashlib
from cryptography.fernet import Fernet, InvalidToken

class SecretCryptoEngineV1:
    def __init__(self, master_key: str = "yasara-local-dev-master-key-change-me"):
        digest = hashlib.sha256(master_key.encode("utf-8")).digest()
        self._fernet = Fernet(base64.urlsafe_b64encode(digest))

    def encrypt(self, value: str) -> str:
        return self._fernet.encrypt(value.encode("utf-8")).decode("utf-8")

    def decrypt(self, encrypted_value: str) -> str:
        try:
            return self._fernet.decrypt(encrypted_value.encode("utf-8")).decode("utf-8")
        except InvalidToken as exc:
            raise ValueError("Invalid encrypted secret or master key.") from exc
