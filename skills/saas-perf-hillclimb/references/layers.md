# Layer guide

Climb in this order. Each layer lists metrics, profiling tools, and candidates ordered cheapest first.

## Database

- Metrics: query P95, queries per request, rows scanned per row returned, lock wait time, connection pool wait.
- Profile: `EXPLAIN (ANALYZE, BUFFERS)`, `pg_stat_statements`, MySQL slow query log, ORM query logging, APM database spans.
- Candidates:
  1. Remove queries whose results are unused.
  2. Fix N+1 patterns with joins or batched loads.
  3. Add or correct indexes for hot filters and sort orders.
  4. Select only needed columns and paginate with keyset cursors.
  5. Cache stable reads with explicit invalidation.
  6. Move heavy reports to read replicas or precomputed tables.
  7. Tune pool size and statement timeouts.

## Backend/API

- Metrics: P50 and P95 response time per endpoint, CPU time per request, allocations, external call time.
- Profile: APM traces, flame graphs (`py-spy`, `pprof`, `clinic`, `async-profiler`), request timing middleware.
- Candidates:
  1. Remove unused work from the request path.
  2. Memoize repeated computation within a request.
  3. Run independent I/O concurrently.
  4. Move slow side effects to background jobs.
  5. Add response caching with correct keys and TTLs.
  6. Reduce payload size and serialization cost.
  7. Reuse HTTP and database connections.

## Frontend

- Metrics: LCP, CLS, INP, JavaScript bytes, long tasks, time to interactive.
- Profile: Lighthouse, WebPageTest, Chrome Performance panel, bundle analyzers, real-user monitoring.
- Candidates:
  1. Remove unused dependencies and code.
  2. Split code by route and lazy-load below-the-fold UI.
  3. Prioritize the LCP resource and preload critical assets.
  4. Reserve space for images, ads, and embeds to stop layout shift.
  5. Compress and resize images; serve modern formats.
  6. Defer third-party scripts.
  7. Virtualize long lists and reduce re-renders.

## CDN/edge

- Metrics: cache hit ratio, time to first byte by region, origin request rate, bytes transferred.
- Profile: CDN analytics, response headers (`cache-control`, `age`, `cf-cache-status`), regional synthetic checks.
- Candidates:
  1. Set long cache lifetimes on hashed static assets.
  2. Cache public HTML or API responses with correct `Vary` keys.
  3. Enable Brotli or gzip compression.
  4. Use HTTP/2 or HTTP/3.
  5. Move redirects and simple rewrites to the edge.

## Infrastructure

- Metrics: CPU and memory saturation, cold start time, queue depth, autoscaling lag.
- Profile: platform metrics, container stats, function cold-start logs.
- Candidates:
  1. Remove idle or duplicate workloads.
  2. Right-size instances and memory limits.
  3. Tune autoscaling thresholds and minimum instances.
  4. Co-locate services and data in one region.
  Do not purchase capacity without user approval.

## Load

- Metrics: throughput at target latency, error rate at 2x expected peak, saturation point.
- Profile: k6, Locust, Artillery, or JMeter with realistic tenant mix, run against a non-production environment.
- Candidates: apply the earlier layers' fixes to the first resource that saturates. Re-run the load test after each kept change.

## Monitoring

After the climb, keep the gains visible:

1. Add dashboards for each climbed metric.
2. Add alerts at the ceiling.
3. Add a performance budget check where the repository's gates allow it.