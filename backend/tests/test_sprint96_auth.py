from app.cloud_v1.auth import AuthServiceV1, UserAccountV1

def test_auth_create_session():
    session = AuthServiceV1().create_session(UserAccountV1(user_id="u1", email="a@b.com"))
    assert session.user_id == "u1"
