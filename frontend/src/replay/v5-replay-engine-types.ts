export type YaSaraReplaySession = { sessionId: string; symbol: string; timeframe: string; speed: number; cursor: number; playing: boolean; };
export type YaSaraReplayEvent = { index: number; eventType: string; payload: Record<string, unknown>; timestamp: string; };
export type YaSaraReplayPlaybackState = { sessionId: string; cursor: number; totalEvents: number; playing: boolean; speed: number; };
