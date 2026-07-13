from pydantic import BaseModel, Field

class MigrationStepV1(BaseModel):
    step_id: str
    description: str
    reversible: bool = True

class MigrationPlanV1(BaseModel):
    from_version: str
    to_version: str
    steps: list[MigrationStepV1] = Field(default_factory=list)

class MigrationEngineV1:
    def plan(self, from_version: str, to_version: str) -> MigrationPlanV1:
        return MigrationPlanV1(from_version=from_version, to_version=to_version, steps=[
            MigrationStepV1(step_id="backup", description="Create pre-upgrade backup"),
            MigrationStepV1(step_id="config", description="Validate production configuration"),
            MigrationStepV1(step_id="schema", description="Apply database migrations", reversible=False),
        ])
