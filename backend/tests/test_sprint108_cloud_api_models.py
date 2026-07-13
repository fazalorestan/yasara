from app.cloud_v1.auth import AuthServiceV1, UserAccountV1

def test_cloud_api_session_model():
    session = AuthServiceV1().create_session(UserAccountV1(user_id="u1", email="x@y.com"))
    assert session.session_id == "session_u1"
