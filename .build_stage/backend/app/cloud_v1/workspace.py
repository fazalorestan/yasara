from pydantic import BaseModel, Field

class CloudWorkspaceV1(BaseModel):
    workspace_id: str
    owner_id: str
    name: str
    members: list[str] = Field(default_factory=list)

class CloudWorkspaceServiceV1:
    def add_member(self, workspace: CloudWorkspaceV1, user_id: str) -> CloudWorkspaceV1:
        if user_id not in workspace.members:
            workspace.members.append(user_id)
        return workspace
