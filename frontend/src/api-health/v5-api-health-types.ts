export type YaSaraAPIEndpointHealth = {
  path: string;
  method: "GET" | "POST" | "PUT" | "DELETE";
  critical: boolean;
  passed: boolean;
};

export type YaSaraAPIHealthReport = {
  ready: boolean;
  failedCount: number;
  total: number;
  executionAllowed: false;
};
