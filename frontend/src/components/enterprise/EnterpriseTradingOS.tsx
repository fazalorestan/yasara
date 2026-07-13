import { useEffect, useMemo, useState } from "react";
import {
  getTradingOSSnapshot,
  type TradingOSSnapshot,
  type WorkspaceName,
} from "../../api/enterpriseTradingOS";
import "../../styles/enterprise-trading-os.css";

const workspaceLabels: Record<WorkspaceName, string> = {
  trader: "Trader",
  ai: "AI Analyst",
  portfolio: "Portfolio",
  developer: "Developer",
};

function Value({ value }: { value: unknown }) {
  if (value === null || value === undefined || value === "") {
    return <span className="etos-unavailable">Waiting for backend data</span>;
  }
  if (typeof value === "object") {
    return <code>{JSON.stringify(value)}</code>;
  }
  return <>{String(value)}</>;
}

export function EnterpriseTradingOS() {
  const [active, setActive] = useState<WorkspaceName>("trader");
  const [snapshot, setSnapshot] = useState<TradingOSSnapshot | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let alive = true;
    const load = async () => {
      try {
        const data = await getTradingOSSnapshot();
        if (alive) {
          setSnapshot(data);
          setError(null);
        }
      } catch (exc) {
        if (alive) setError(exc instanceof Error ? exc.message : String(exc));
      } finally {
        if (alive) setLoading(false);
      }
    };
    void load();
    const timer = window.setInterval(load, 10_000);
    return () => {
      alive = false;
      window.clearInterval(timer);
    };
  }, []);

  const workspace = useMemo(
    () => snapshot?.workspaces.find((item) => item.workspace === active),
    [snapshot, active],
  );

  return (
    <section className="etos-shell">
      <header className="etos-header">
        <div>
          <small>YaSara Enterprise</small>
          <h1>Trading Operating System</h1>
        </div>
        <div className="etos-build">
          <span className={snapshot?.ready ? "ok" : "warn"}>
            {snapshot?.ready ? "● Runtime Ready" : "● Runtime Pending"}
          </span>
          <b>{snapshot?.build_id ?? "Build unavailable"}</b>
        </div>
      </header>

      <nav className="etos-workspaces" aria-label="Trading OS workspaces">
        {(Object.keys(workspaceLabels) as WorkspaceName[]).map((name) => (
          <button
            key={name}
            className={active === name ? "active" : ""}
            onClick={() => setActive(name)}
          >
            {workspaceLabels[name]}
          </button>
        ))}
      </nav>

      {loading && <div className="etos-state">Loading real backend state…</div>}
      {error && <div className="etos-state error">{error}</div>}

      {!loading && !error && workspace && (
        <>
          <section className="etos-metrics">
            {workspace.metrics.map((metric) => (
              <article key={metric.key} className="etos-card etos-metric">
                <span>{metric.label}</span>
                <strong><Value value={metric.value} /></strong>
                <small>Source: {metric.source}</small>
              </article>
            ))}
          </section>

          <section className="etos-grid">
            {Object.entries(workspace.panels).map(([key, value]) => (
              <article className="etos-card etos-panel" key={key}>
                <header>
                  <h2>{key.split("_").join(" ")}</h2>
                  <span>Live backend</span>
                </header>
                <div className="etos-panel-body">
                  <Value value={value} />
                </div>
              </article>
            ))}
          </section>
        </>
      )}

      <footer className="etos-footer">
        <span>Real backend data only</span>
        <span>Signal Only: {snapshot?.signal_only_default ? "ON" : "OFF"}</span>
        <span>Auto Trading: {snapshot?.auto_trading_enabled ? "ON" : "OFF"}</span>
        <span>Doctor: {snapshot?.doctor && Object.keys(snapshot.doctor).length ? "Integrated" : "Pending"}</span>
      </footer>
    </section>
  );
}
