from pydantic import BaseModel, Field

class APITokenV1(BaseModel):
    token_id: str
    owner_id: str
    scopes: list[str] = Field(default_factory=list)
    active: bool = True

class APITokenServiceV1:
    def can(self, token: APITokenV1, scope: str) -> bool:
        return token.active and scope in token.scopes
