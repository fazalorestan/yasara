import { apiGet } from "./client";

export const getPhaseAMetaSummary = () =>
  apiGet("/v3-6/phase-a-meta-ykb/summary");

export const getPhaseAMetaHealth = () =>
  apiGet("/v3-6/phase-a-meta-ykb/health");

export const getYkbStatus = () =>
  apiGet("/v3-6/phase-a-meta-ykb/ykb/status");

export const getPhaseARecommendations = () =>
  apiGet("/v3-6/phase-a-meta-ykb/recommendations");
