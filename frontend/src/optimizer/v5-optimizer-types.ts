export type YaSaraOptimizationConfig = { strategyId: string; symbol: string; objective: string; maxTrials: number; executionAllowed: false; };
export type YaSaraOptimizationTrial = { trialId: string; parameters: Record<string, unknown>; score: number; metrics: Record<string, unknown>; };
export type YaSaraOptimizerRun = { ready: boolean; best: YaSaraOptimizationTrial | null; totalTrials: number; executionAllowed: false; };
