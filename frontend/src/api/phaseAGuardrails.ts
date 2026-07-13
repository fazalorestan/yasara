import { apiGet } from "./client";

export const getPhaseAGuardrailsSummary = () =>
  apiGet("/v3-6-1/phase-a-guardrails/summary");

export const getPhaseAGuardrailsHealth = () =>
  apiGet("/v3-6-1/phase-a-guardrails/health");

export const getYkbStats = () =>
  apiGet("/v3-6-1/phase-a-guardrails/ykb/stats");

export const getGuardrailRecommendations = () =>
  apiGet("/v3-6-1/phase-a-guardrails/recommendations");
