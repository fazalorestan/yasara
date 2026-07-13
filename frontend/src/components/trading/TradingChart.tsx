import { useEffect, useRef } from "react";
import {
  createChart,
  ColorType,
  IChartApi,
  UTCTimestamp
} from "lightweight-charts";
import { buildDemoCandles, buildDemoVolumes } from "../../data/tradingTerminal";

interface TradingChartProps {
  seed: number;
}

export function TradingChart({ seed }: TradingChartProps) {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const chartRef = useRef<IChartApi | null>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    const candles = buildDemoCandles(seed);
    const volumes = buildDemoVolumes(candles);

    const chart = createChart(containerRef.current, {
      autoSize: true,
      height: 520,
      layout: {
        background: { type: ColorType.Solid, color: "#070b14" },
        textColor: "#94a3b8"
      },
      grid: {
        vertLines: { color: "rgba(148, 163, 184, 0.08)" },
        horzLines: { color: "rgba(148, 163, 184, 0.08)" }
      },
      rightPriceScale: { borderColor: "rgba(148, 163, 184, 0.18)" },
      timeScale: { borderColor: "rgba(148, 163, 184, 0.18)" },
      crosshair: { mode: 1 }
    });

    const candleSeries = chart.addCandlestickSeries({
      upColor: "#22c55e",
      downColor: "#ef4444",
      borderUpColor: "#22c55e",
      borderDownColor: "#ef4444",
      wickUpColor: "#22c55e",
      wickDownColor: "#ef4444"
    });

    candleSeries.setData(
  candles.map(c => ({
    ...c,
    time: c.time as UTCTimestamp
  }))
);

    chart.priceScale("").applyOptions({
  scaleMargins: {
    top: 0.82,
    bottom: 0
  }
});

const volumeSeries = chart.addHistogramSeries({
  priceFormat: { type: "volume" },
  priceScaleId: ""
});

volumeSeries.setData(
  volumes.map(v => ({
    ...v,
    time: v.time as UTCTimestamp
  }))
);
    chart.timeScale().fitContent();
    chartRef.current = chart;

    const resize = () => chart.applyOptions({ width: containerRef.current?.clientWidth ?? 0 });
    window.addEventListener("resize", resize);

    return () => {
      window.removeEventListener("resize", resize);
      chart.remove();
      chartRef.current = null;
    };
  }, [seed]);

  return <div className="trading-chart" ref={containerRef} />;
}
