import {
  LineChart,
  BrainCircuit,
  Wallet,
  FlaskConical,
  Zap,
  BookOpen,
  Code2,
  Search,
  Boxes,
  HeartPulse,
  Settings2,
  Flag,
  Clock,
  Radio,
  FileText,
  BarChart3,
  Settings,
  ChevronDown,
  Menu,
} from "lucide-react";
import type { ComponentType } from "react";

export type Workspace =
  | "market"
  | "ai"
  | "portfolio"
  | "strategy"
  | "trading"
  | "journal"
  | "developer";

export interface SidebarWatchItem {
  symbol: string;
  price: string;
  change: string;
  direction: "up" | "down";
}

interface SidebarProps {
  workspace: Workspace;
  setWorkspace: (w: Workspace) => void;
  collapsed: boolean;
  onToggleCollapsed: () => void;
  onOpenSettings: () => void;
  watchlist?: SidebarWatchItem[];
  version?: string;
}

const WORKSPACE_NAV: Array<{ key: Workspace; label: string; icon: ComponentType<{ size?: number }> }> = [
  { key: "market", label: "Market Workspace", icon: LineChart },
  { key: "ai", label: "AI Workspace", icon: BrainCircuit },
  { key: "portfolio", label: "Portfolio Workspace", icon: Wallet },
  { key: "strategy", label: "Strategy Workspace", icon: FlaskConical },
  { key: "trading", label: "Live Trading Workspace", icon: Zap },
  { key: "journal", label: "Journal Workspace", icon: BookOpen },
  { key: "developer", label: "Developer Workspace", icon: Code2 },
];

const PLATFORM_LINKS: Array<{ label: string; icon: ComponentType<{ size?: number }> }> = [
  { label: "Discovery", icon: Search },
  { label: "Registry", icon: Boxes },
  { label: "Health", icon: HeartPulse },
  { label: "Configuration", icon: Settings2 },
  { label: "Feature Flags", icon: Flag },
  { label: "Scheduler", icon: Clock },
  { label: "Event Bus", icon: Radio },
];

const SYSTEM_LINKS: Array<{ label: string; icon: ComponentType<{ size?: number }> }> = [
  { label: "Documentation", icon: FileText },
  { label: "Reports", icon: BarChart3 },
];

export function Sidebar({
  workspace,
  setWorkspace,
  collapsed,
  onToggleCollapsed,
  onOpenSettings,
  watchlist = [],
  version = "YaSara v4.42",
}: SidebarProps) {
  return (
    <aside className={`ent-sidebar ${collapsed ? "collapsed" : ""}`}>
      <div className="ent-brand">
        <button className="ent-menu-btn" onClick={onToggleCollapsed} aria-label="Toggle sidebar">
          <Menu size={18} />
        </button>
        <div className="ent-brand-mark">A</div>
        {!collapsed && (
          <div className="ent-brand-text">
            <strong>YaSara</strong>
            <span>Enterprise Edition</span>
          </div>
        )}
      </div>

      <nav className="ent-nav-scroll">
        <div className="ent-nav-section">
          {!collapsed && <span className="ent-nav-label">Workspaces</span>}
          {WORKSPACE_NAV.map(({ key, label, icon: Icon }) => (
            <button
              key={key}
              className={`ent-nav-item ${workspace === key ? "active" : ""}`}
              onClick={() => setWorkspace(key)}
              title={label}
            >
              <Icon size={17} />
              {!collapsed && <span>{label}</span>}
            </button>
          ))}
        </div>

        <div className="ent-nav-section">
          {!collapsed && <span className="ent-nav-label">Platform</span>}
          {PLATFORM_LINKS.map(({ label, icon: Icon }) => (
            <button key={label} className="ent-nav-item ent-nav-item-muted" title={label}>
              <Icon size={16} />
              {!collapsed && <span>{label}</span>}
            </button>
          ))}
        </div>

        <div className="ent-nav-section">
          {!collapsed && <span className="ent-nav-label">System</span>}
          {SYSTEM_LINKS.map(({ label, icon: Icon }) => (
            <button key={label} className="ent-nav-item ent-nav-item-muted" title={label}>
              <Icon size={16} />
              {!collapsed && <span>{label}</span>}
            </button>
          ))}
          <button className="ent-nav-item ent-nav-item-muted" title="Settings" onClick={onOpenSettings}>
            <Settings size={16} />
            {!collapsed && <span>Settings</span>}
          </button>
        </div>
      </nav>

      {!collapsed && watchlist.length > 0 && (
        <div className="ent-sidebar-watch">
          {watchlist.slice(0, 4).map((item) => (
            <div key={item.symbol} className="ent-sidebar-watch-row">
              <span>{item.symbol}</span>
              <strong>{item.price}</strong>
              <em className={item.direction}>{item.change}</em>
            </div>
          ))}
        </div>
      )}

      <footer className="ent-sidebar-footer">
        {!collapsed ? (
          <>
            <span>{version}</span>
            <span className="ent-sidebar-sub">Enterprise Platform</span>
          </>
        ) : (
          <ChevronDown size={14} />
        )}
      </footer>
    </aside>
  );
}
