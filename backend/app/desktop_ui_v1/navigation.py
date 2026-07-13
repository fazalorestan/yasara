from pydantic import BaseModel

class NavigationItemV1(BaseModel):
    route: str
    title: str
    icon: str = ""

class NavigationBuilderV1:
    def main(self) -> list[NavigationItemV1]:
        return [
            NavigationItemV1(route="/dashboard", title="Dashboard", icon="dashboard"),
            NavigationItemV1(route="/backtest", title="Backtest", icon="science"),
            NavigationItemV1(route="/settings", title="Settings", icon="settings"),
        ]
