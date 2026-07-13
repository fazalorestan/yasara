export interface ApprovedDashboardSnapshot {
  build_id: string;
  approved_dashboard_locked: boolean;
  real_data_only: boolean;
  mock_data: boolean;
  signal_only_default: boolean;
  auto_trading_enabled: boolean;
  providers: unknown[];
  widgets: Record<string, unknown>;
}
export async function getApprovedDashboardSnapshot(): Promise<ApprovedDashboardSnapshot> {
  const response = await fetch("/api/v1/enterprise/dashboard-hub/snapshot", {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) throw new Error(`Dashboard hub failed: ${response.status}`);
  return response.json();
}
