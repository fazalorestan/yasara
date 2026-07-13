export type YaSaraRuntimeEndpoint = { path: string; method: "GET"; critical: boolean; };
export type YaSaraRuntimeAPISmokeResult = { path: string; passed: boolean; critical: boolean; };
export type YaSaraRuntimeAPISmokeReadiness = { ready: boolean; score: number; executionAllowed: false; };
