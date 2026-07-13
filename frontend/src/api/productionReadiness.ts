import { apiGet } from "./client";

export const getProductionReadinessSummary = () =>
  apiGet("/v4-8/production-readiness/summary");

export const getFinalReadiness = () =>
  apiGet("/v4-8/production-readiness/final-readiness");
