from app.v52_enterprise_workspaces.models import WorkspaceDescriptor
from app.v52_enterprise_workspaces.registry import workspace_registry

DEFAULT_WORKSPACES = [
    WorkspaceDescriptor(id="dashboard", title="Dashboard", icon="dashboard", order=10, route="/", source="enterprise_dashboard", capabilities=["summary","widgets","doctor"]),
    WorkspaceDescriptor(id="trading", title="Trading", icon="candlestick", order=20, route="/trading", source="trading_os", capabilities=["signals","confirmations","portfolio","risk"]),
    WorkspaceDescriptor(id="ai", title="AI", icon="brain", order=30, route="/ai", source="ai_decision_core", capabilities=["decision","explainability","timeline"]),
    WorkspaceDescriptor(id="portfolio", title="Portfolio", icon="portfolio", order=40, route="/portfolio", source="portfolio_engine", capabilities=["allocation","exposure","drawdown"]),
    WorkspaceDescriptor(id="life", title="Life Management", icon="life", order=50, route="/life", source="life_workspace", capabilities=["calendar","tasks","finance","projects"]),
    WorkspaceDescriptor(id="developer", title="Developer", icon="code", order=90, route="/developer", source="developer_workspace", capabilities=["registry","logs","build","health"]),
]

def bootstrap_workspaces():
    for descriptor in DEFAULT_WORKSPACES:
        workspace_registry.register(descriptor)

bootstrap_workspaces()
