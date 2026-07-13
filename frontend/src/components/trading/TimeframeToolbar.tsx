import type { Timeframe } from "../../data/tradingTerminal";
import { timeframes } from "../../data/tradingTerminal";

interface TimeframeToolbarProps {
  value: Timeframe;
  onChange: (timeframe: Timeframe) => void;
}

export function TimeframeToolbar({ value, onChange }: TimeframeToolbarProps) {
  return (
    <div className="timeframe-toolbar">
      {timeframes.map((tf) => (
        <button key={tf} className={tf === value ? "tf active" : "tf"} onClick={() => onChange(tf)}>
          {tf}
        </button>
      ))}
    </div>
  );
}
