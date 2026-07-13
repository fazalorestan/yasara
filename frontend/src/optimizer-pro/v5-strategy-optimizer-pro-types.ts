export type YaSaraOptimizerProTrial = { trialId: string; parameters: Record<string, unknown>; metrics: Record<string, number>; score: number; robustnessGrade: string; };
export type YaSaraOptimizerProReport = { ready: boolean; trialCount: number; best: YaSaraOptimizerProTrial | null; researchOnly: true; executionAllowed: false; };
