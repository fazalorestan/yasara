from app.productivity_v1.preferences import UserPreferencesServiceV1, UserPreferencesV1

def test_user_preferences_update():
    prefs = UserPreferencesServiceV1().update(UserPreferencesV1(), default_exchange="toobit")
    assert prefs.default_exchange == "toobit"
