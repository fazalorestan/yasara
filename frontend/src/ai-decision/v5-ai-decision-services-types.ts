export type YaSaraAIConsensus = { ready: boolean; direction: string; agreementPct: number; votes: Record<string, number>; };
export type YaSaraAIPipelineDecision = { symbol: string; direction: string; confidence: number; executionAllowed: false; };
export type YaSaraAIQualityGate = { ready: boolean; passed: boolean; confidence: number; agreementPct: number; executionAllowed: false; };
