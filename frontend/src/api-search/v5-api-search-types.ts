export type YaSaraAPIEndpointSearchItem = { path: string; tag: string; summary: string; };
export type YaSaraAPIEndpointSearchResult = { ready: boolean; query: string; count: number; items: YaSaraAPIEndpointSearchItem[]; };
export type YaSaraStartupSelfTest = { ready: boolean; checks: Record<string, boolean>; };
