export interface WorkspacePreset {
  id: string;
  name: string;
  description: string;
  active?: boolean;
}

export interface ThemeOption {
  id: string;
  name: string;
  accent: string;
}

export const workspacePresets: WorkspacePreset[] = [
  { id: "terminal", name: "Trading Terminal", description: "Chart, order book, portfolio and live events.", active: true },
  { id: "analysis", name: "AI Analysis", description: "AI signals, regime, risk and market overview." },
  { id: "execution", name: "Paper Execution", description: "Positions, orders and paper order panel." }
];

export const themeOptions: ThemeOption[] = [
  { id: "professional", name: "Professional Dark", accent: "#38bdf8" },
  { id: "oled", name: "OLED Black", accent: "#22c55e" },
  { id: "violet", name: "Violet Pro", accent: "#8b5cf6" }
];

export const productionChecklist = [
  { label: "Backend API", done: true },
  { label: "React dashboard", done: true },
  { label: "Safe mode", done: true },
  { label: "Live trading disabled", done: true },
  { label: "Production build ready", done: true }
];
