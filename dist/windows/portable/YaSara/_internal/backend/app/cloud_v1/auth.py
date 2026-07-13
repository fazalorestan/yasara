from pydantic import BaseModel

class UserAccountV1(BaseModel):
    user_id: str
    email: str
    active: bool = True

class AuthSessionV1(BaseModel):
    session_id: str
    user_id: str
    expires_in_seconds: int = 3600

class AuthServiceV1:
    def create_session(self, user: UserAccountV1) -> AuthSessionV1:
        return AuthSessionV1(session_id=f"session_{user.user_id}", user_id=user.user_id)
