import type { ReactNode } from "react";

export interface PanelProps {
  title: string;
  action?: ReactNode;
  status?: { label: string; tone: "up" | "down" | "neutral" | "warning" };
  className?: string;
  children: ReactNode;
  bodyClassName?: string;
}

export function Panel({ title, action, status, className = "", children, bodyClassName = "" }: PanelProps) {
  return (
    <section className={`ent-panel ${className}`}>
      <div className="ent-panel-head">
        <div className="ent-panel-title">
          <h2>{title}</h2>
          {status && <span className={`ent-panel-status status-${status.tone}`}>{status.label}</span>}
        </div>
        {action && <div className="ent-panel-action">{action}</div>}
      </div>
      <div className={`ent-panel-body ${bodyClassName}`}>{children}</div>
    </section>
  );
}
