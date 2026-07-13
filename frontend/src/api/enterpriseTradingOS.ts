export type WorkspaceName = "trader" | "ai" | "portfolio" | "developer";

export interface MetricValue {
  key: string;
  label: string;
  value: unknown;
  status: string;
  source: string;
  updated_at?: number | null;
}

export interface WorkspaceSnapshot {
  workspace: WorkspaceName;
  ready: boolean;
  metrics: MetricValue[];
  panels: Record<string, unknown>;
}

export interface TradingOSSnapshot {
  build_id: string;
  ready: boolean;
  real_data_only: boolean;
  mock_data: boolean;
  signal_only_default: boolean;
  auto_trading_enabled: boolean;
  workspaces: WorkspaceSnapshot[];
  doctor: Record<string, unknown>;
  runtime: Record<string, unknown>;
}

export async function getTradingOSSnapshot(): Promise<TradingOSSnapshot> {
  const response = await fetch("/api/v1/enterprise/trading-os/snapshot", {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    throw new Error(`Trading OS snapshot failed: ${response.status}`);
  }
  return response.json();
}
