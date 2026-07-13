import { useEffect, useMemo, useState } from "react";
import {
  getAIFirstDashboardSnapshot,
  type AIFirstDashboardSnapshot,
} from "../../api/aiFirstDashboard";
import "../../styles/ai-first-dashboard.css";

function DataValue({ value }: { value: unknown }) {
  if (value === null || value === undefined || value === "") {
    return <span className="afd-waiting">Waiting for real data</span>;
  }
  if (typeof value === "object") {
    return <pre>{JSON.stringify(value, null, 2)}</pre>;
  }
  return <>{String(value)}</>;
}

export function AIFirstDashboard() {
  const [snapshot, setSnapshot] = useState<AIFirstDashboardSnapshot | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;

    const load = async () => {
      try {
        const data = await getAIFirstDashboardSnapshot();
        if (active) {
          setSnapshot(data);
          setError(null);
        }
      } catch (exc) {
        if (active) {
          setError(exc instanceof Error ? exc.message : String(exc));
        }
      }
    };

    void load();
    const timer = window.setInterval(load, 5000);

    return () => {
      active = false;
      window.clearInterval(timer);
    };
  }, []);

  const byKey = useMemo(() => {
    const map = new Map<string, AIFirstDashboardSnapshot["sections"][number]>();
    snapshot?.sections.forEach((section) => map.set(section.key, section));
    return map;
  }, [snapshot]);

  if (error) return <div className="afd-error">{error}</div>;
  if (!snapshot) return <div className="afd-loading">Loading real backend data…</div>;

  return (
    <main className="afd-shell">
      <header className="afd-topbar">
        <div>
          <small>YaSara Enterprise</small>
          <h1>AI-First Trading Dashboard</h1>
        </div>
        <div className="afd-build">{snapshot.build_id}</div>
      </header>

      <section className="afd-kpis">
        {snapshot.metrics.map((metric) => (
          <article className="afd-card afd-kpi" key={metric.key}>
            <span>{metric.label}</span>
            <strong><DataValue value={metric.value} /></strong>
            <small>{metric.source}</small>
          </article>
        ))}
      </section>

      <section className="afd-main-grid">
        <article className="afd-card afd-signal">
          <h2>AI Signal Matrix</h2>
          <DataValue value={byKey.get("ai_signal_matrix")?.payload} />
        </article>

        <article className="afd-card afd-confirmations">
          <h2>Confirmations</h2>
          <DataValue value={byKey.get("confirmations")?.payload} />
        </article>

        <article className="afd-card afd-chart">
          <h2>Market Chart</h2>
          <DataValue value={byKey.get("market_chart")?.payload} />
        </article>

        <article className="afd-card">
          <h2>Risk Engine</h2>
          <DataValue value={byKey.get("risk_engine")?.payload} />
        </article>

        <article className="afd-card">
          <h2>Portfolio</h2>
          <DataValue value={byKey.get("portfolio")?.payload} />
        </article>

        <article className="afd-card">
          <h2>Developer Health</h2>
          <DataValue value={byKey.get("developer_health")?.payload} />
        </article>
      </section>

      <footer className="afd-footer">
        <span>Real backend data only</span>
        <span>Signal Only: {snapshot.signal_only_default ? "ON" : "OFF"}</span>
        <span>Auto Trading: {snapshot.auto_trading_enabled ? "ON" : "OFF"}</span>
      </footer>
    </main>
  );
}
