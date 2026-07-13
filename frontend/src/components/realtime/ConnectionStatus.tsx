import { Radio, RefreshCcw, WifiOff } from "lucide-react";
import type { ConnectionState } from "../../data/realtimeIntelligence";

interface ConnectionStatusProps {
  state: ConnectionState;
  statusText: string;
  lastUpdate: Date;
}

export function ConnectionStatus({ state, statusText, lastUpdate }: ConnectionStatusProps) {
  const Icon = state === "connected" ? Radio : state === "reconnecting" ? RefreshCcw : WifiOff;

  return (
    <div className={`connection-status ${state}`}>
      <Icon size={16} />
      <div>
        <strong>{statusText}</strong>
        <span>Last update: {lastUpdate.toLocaleTimeString()}</span>
      </div>
    </div>
  );
}
