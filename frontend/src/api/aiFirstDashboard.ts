export interface DashboardMetric {
  key: string;
  label: string;
  value: unknown;
  status: string;
  source: string;
  updated_at?: number | null;
}

export interface DashboardSection {
  key: string;
  title: string;
  status: string;
  source: string;
  payload: Record<string, unknown>;
}

export interface AIFirstDashboardSnapshot {
  build_id: string;
  ready: boolean;
  real_data_only: boolean;
  mock_data: boolean;
  signal_only_default: boolean;
  auto_trading_enabled: boolean;
  metrics: DashboardMetric[];
  sections: DashboardSection[];
  doctor: Record<string, unknown>;
}

export async function getAIFirstDashboardSnapshot(): Promise<AIFirstDashboardSnapshot> {
  const response = await fetch("/api/v1/enterprise/ai-first-dashboard/snapshot", {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    throw new Error(`AI-first dashboard failed: ${response.status}`);
  }
  return response.json();
}
