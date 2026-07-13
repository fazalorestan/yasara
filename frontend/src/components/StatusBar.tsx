import { useResilientResource } from "../hooks/useResilientResource";
import { getFinalOperationalHealth } from "../api/finalOperational";
import "../styles/enterprise-panels.css";

interface HealthSnapshot {
  apiOnline: boolean;
  latencyMs: number | null;
  dataRateMbps: number | null;
  connections: number | null;
  cpuPercent: number | null;
  memoryPercent: number | null;
  diskPercent: number | null;
  uptime: string;
  mode: string;
}

async function fetchHealth(): Promise<HealthSnapshot | null> {
  const res: any = await getFinalOperationalHealth();
  if (res == null) return null;
  return {
    apiOnline: true,
    latencyMs: typeof res.latency_ms === "number" ? res.latency_ms : null,
    dataRateMbps: typeof res.data_rate_mbps === "number" ? res.data_rate_mbps : null,
    connections: typeof res.connections === "number" ? res.connections : null,
    cpuPercent: typeof res.cpu_percent === "number" ? res.cpu_percent : null,
    memoryPercent: typeof res.memory_percent === "number" ? res.memory_percent : null,
    diskPercent: typeof res.disk_percent === "number" ? res.disk_percent : null,
    uptime: res.uptime ?? "Unavailable",
    mode: res.mode ?? "Unavailable",
  };
}

/**
 * Footer status bar. Self-fetches from the existing
 * /v2-6/final-operational/health endpoint via the shared resilient hook.
 * Previously this panel was fed hardcoded numbers from App.tsx (34ms,
 * 128 connections, etc.) - those were fabricated and are removed here.
 * Every field falls back to "--" (already the component's built-in
 * empty-state convention) instead of inventing a value, and the API
 * status dot reflects real connectivity, not a static "Online" claim.
 */
export function StatusBar() {
  const res = useResilientResource<HealthSnapshot>(fetchHealth, { baseIntervalMs: 10000 });
  const d = res.data;

  return (
    <footer className="ent-statusbar-v2">
      <div className="ent-sb-item">
        <span className={`ent-sb-dot ${res.available ? "ok" : ""}`} />
        <span className="ent-sb-label">API Status</span>
        <span className="ent-sb-value">{res.available ? "Online" : "Offline"}</span>
      </div>

      <span className="ent-sb-sep" />

      <div className="ent-sb-item">
        <span className="ent-sb-label">Latency</span>
        <span className="ent-sb-value">{d?.latencyMs != null ? `${d.latencyMs}ms` : "--"}</span>
      </div>

      <div className="ent-sb-item">
        <span className="ent-sb-label">Data Rate</span>
        <span className="ent-sb-value">{d?.dataRateMbps != null ? `${d.dataRateMbps.toFixed(1)} MB/s` : "--"}</span>
      </div>

      <div className="ent-sb-item">
        <span className="ent-sb-label">Connections</span>
        <span className="ent-sb-value">{d?.connections ?? "--"}</span>
      </div>

      <span className="ent-sb-sep" />

      <div className="ent-sb-item">
        <span className="ent-sb-label">CPU Usage</span>
        <span className="ent-sb-value">{d?.cpuPercent != null ? `${d.cpuPercent}%` : "--"}</span>
      </div>

      <div className="ent-sb-item">
        <span className="ent-sb-label">Memory Usage</span>
        <span className="ent-sb-value">{d?.memoryPercent != null ? `${d.memoryPercent}%` : "--"}</span>
      </div>

      <div className="ent-sb-item">
        <span className="ent-sb-label">Disk Usage</span>
        <span className="ent-sb-value">{d?.diskPercent != null ? `${d.diskPercent}%` : "--"}</span>
      </div>

      <span className="ent-sb-sep" />

      <div className="ent-sb-item">
        <span className="ent-sb-label">Uptime</span>
        <span className="ent-sb-value">{d?.uptime ?? "--"}</span>
      </div>

      <div className="ent-sb-mode">{d?.mode ?? "Unavailable"}</div>
      <time className="ent-sb-time">{new Date().toLocaleString()}</time>
    </footer>
  );
}
