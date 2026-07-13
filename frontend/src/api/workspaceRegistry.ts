export interface WorkspaceDescriptor {
  id: string;
  title: string;
  icon: string;
  order: number;
  enabled: boolean;
  route: string;
  source: string;
  health: string;
  permissions: string[];
  capabilities: string[];
}

export interface WorkspaceRegistrySnapshot {
  build_id: string;
  real_data_only: boolean;
  mock_data: boolean;
  dashboard_layout_locked: boolean;
  workspaces: WorkspaceDescriptor[];
  doctor: Record<string, unknown>;
}

export async function getWorkspaceRegistry(): Promise<WorkspaceRegistrySnapshot> {
  const response = await fetch("/api/v1/enterprise/workspaces", {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) throw new Error(`Workspace registry failed: ${response.status}`);
  return response.json();
}
