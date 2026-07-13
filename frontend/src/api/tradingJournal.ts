import { apiGet } from "./client";

export const getTradingJournalSummary = () =>
  apiGet("/v4-6/trading-journal/summary");

export const getTradingJournalStats = () =>
  apiGet("/v4-6/trading-journal/stats");
