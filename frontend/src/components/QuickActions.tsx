import { Plus, Terminal, FlaskConical, Radar, History, ShieldCheck } from "lucide-react";
import type { ComponentType } from "react";
import { Panel } from "./Panel";
import type { Workspace } from "./Sidebar";

interface QuickActionsProps {
  onNavigate?: (workspace: Workspace) => void;
  onNewOrder?: () => void;
}

const ACTIONS: Array<{
  label: string;
  icon: ComponentType<{ size?: number }>;
  target?: Workspace;
  primary?: boolean;
}> = [
  { label: "New Order", icon: Plus, primary: true },
  { label: "Trade Terminal", icon: Terminal, target: "trading" },
  { label: "Strategy Builder", icon: FlaskConical, target: "strategy" },
  { label: "AI Scanner", icon: Radar, target: "ai" },
  { label: "Backtest", icon: History, target: "strategy" },
  { label: "Risk Manager", icon: ShieldCheck, target: "portfolio" },
];

export function QuickActions({ onNavigate, onNewOrder }: QuickActionsProps) {
  return (
    <Panel title="Quick Actions">
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
        {ACTIONS.map(({ label, icon: Icon, target, primary }) => (
          <button
            key={label}
            onClick={() => (target ? onNavigate?.(target) : onNewOrder?.())}
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "flex-start",
              gap: 6,
              padding: "10px 10px",
              borderRadius: 8,
              cursor: "pointer",
              fontSize: 12,
              border: primary ? "none" : "1px solid var(--ent-border, rgba(255,255,255,0.08))",
              background: primary ? "var(--ent-accent, #6f5cf0)" : "rgba(255,255,255,0.03)",
              color: primary ? "#fff" : "inherit",
            }}
          >
            <Icon size={16} />
            <span>{label}</span>
          </button>
        ))}
      </div>
    </Panel>
  );
}
