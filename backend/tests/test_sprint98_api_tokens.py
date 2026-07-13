from app.cloud_v1.api_tokens import APITokenServiceV1, APITokenV1

def test_api_token_scope():
    token = APITokenV1(token_id="t1", owner_id="u1", scopes=["read"])
    assert APITokenServiceV1().can(token, "read") is True
    assert APITokenServiceV1().can(token, "write") is False
