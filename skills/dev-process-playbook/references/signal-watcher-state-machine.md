# Starter model: ATAS signal watcher (adapt to the real code)
States: Idle, TradeSeen, Validated, Queued, Sent, Expired, Dropped, Held (feed lost or reloading).
Events: NewTrade, ValidateOk, ValidateFail, QueueFull, SendOk, SendFail, Timeout, ConnectionLost, ConnectionBack, ChartReload.
Rules that must always hold:
1. A signal is sent at most once.
2. An expired signal (age by MarketTime over the limit) is never sent.
3. Every signal ends in Sent, Expired or Dropped, with a logged reason.
4. While Held, no new signal is sent; on ConnectionBack, stale signals are expired, not sent.
5. Age is always MarketTime minus trade.Time, never the PC clock.
Measure per signal: trade.Time, MarketTime on arrival, MarketTime when sent, PC clock (for comparison only).
Next steps: write the TLA+ spec from this, run TLC, add the counterexamples as replay tests.
