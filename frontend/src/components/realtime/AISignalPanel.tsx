import { Brain } from "lucide-react";
import { aiSignals } from "../../data/realtimeIntelligence";

export function AISignalPanel() {
  return (
    <div className="ai-signal-panel">
      {aiSignals.map((signal) => (
        <div className={`ai-signal ${signal.state}`} key={signal.symbol}>
          <div>
            <strong><Brain size={14} /> {signal.symbol}</strong>
            <span>{signal.reason}</span>
          </div>
          <b>{signal.confidence}%</b>
        </div>
      ))}
    </div>
  );
}
