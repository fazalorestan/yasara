export type YaSaraExchangeLifecycleState =
  | "discovered"
  | "registered"
  | "initialized"
  | "ready"
  | "connected"
  | "disconnected"
  | "failed"
  | "recovering"
  | "shutdown";

export type YaSaraExchangeConnectorState = {
  exchangeId: string;
  state: YaSaraExchangeLifecycleState;
  realConnection: false;
  executionAllowed: false;
};

export type YaSaraExchangeHealthMetrics = {
  heartbeatCount: number;
  reconnectCount: number;
  failureCount: number;
  lastSuccess: string | null;
  lastError: string | null;
  averageLatencyMs: number;
  availability: number;
};
