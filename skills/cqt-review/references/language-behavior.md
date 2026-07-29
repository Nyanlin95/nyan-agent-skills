# Language behavior

Use this reference when language semantics affect correctness, ownership, state, failure, concurrency, or migration behavior.

Treat each profile as a review map, not a complete language specification. Confirm version-specific behavior in the repository toolchain or primary documentation.

Use the repository's pinned documentation first. Use the official links in this file when the repository does not answer the question.

## Review method

1. Identify the language, version, runtime, compiler, and important flags.
2. Separate compile-time guarantees from runtime behavior.
3. Trace ownership, mutation, cleanup, errors, concurrency, and module initialization.
4. Check framework behavior only after language behavior is clear.
5. Cite the code path, configuration, or primary documentation that proves the finding.
6. State uncertainty when behavior depends on a version, feature flag, target, or runtime.

Do not report a finding only because another language uses a different convention.

## JavaScript and TypeScript

- TypeScript types do not exist at runtime unless code adds runtime validation.
- Structural typing can accept values with extra fields or compatible shapes.
- `undefined`, missing properties, and `null` can represent different states.
- Objects, arrays, maps, and sets use reference semantics and permit shared mutation.
- Creating a native `Promise` invokes its executor immediately. A promise does not provide automatic cancellation.
- `async` functions return promises. A thrown value becomes a rejected promise.
- The event loop does not make multi-step state changes atomic.
- Module top-level code runs during module evaluation and can create order-dependent side effects.
- ESM and CommonJS interoperation depends on the runtime, package configuration, and build tool.
- Type assertions and non-null assertions suppress checks. They do not validate data.

Review trust boundaries for runtime validation. Review asynchronous workflows for stale results, unhandled rejection, cancellation, and partial effects.

## Rust

- Ownership and borrowing control memory access. Interior mutability can move checks to runtime.
- `Option` represents absence. `Result` represents recoverable failure by convention.
- `panic!` is not a normal error return. The profile can unwind or abort.
- `Drop` runs during normal scope exit and unwinding. It does not run after an abort.
- `Send` and `Sync` control cross-thread use. They do not prove higher-level workflow safety.
- Futures make progress when polled. Dropping a future cancels it only through drop behavior.
- Async cancellation can leave external effects complete and later steps unfinished.
- `unsafe` moves proof obligations to the programmer and its safe wrapper.
- Feature flags and target-specific compilation can produce different program shapes.
- Poisoning, lock scope, and blocking work inside async code can change failure or liveness behavior.

Review unsafe boundaries, cancellation safety, lock scope, error translation, feature combinations, and ownership of external effects.

## Python

- Type hints do not enforce runtime types unless another tool validates them.
- Default argument expressions run once when Python defines the function.
- Names reference objects. Mutable objects can be shared across callers.
- Exceptions can leave earlier mutations or external effects complete.
- Context managers own deterministic cleanup around a scope.
- Imports execute module top-level code once per interpreter module instance.
- `asyncio` tasks use cooperative scheduling. Blocking calls can stop event-loop progress.
- `Task.cancel()` requests cancellation by scheduling `CancelledError`. Cleanup code can catch or defer it.
- The GIL does not make compound operations or external resources transaction-safe.
- Multiprocessing uses separate memory and serialization rules.

Review mutable defaults, import effects, exception cleanup, task ownership, blocking calls, and process boundaries.

## Go

- Errors are ordinary return values. Ignored or wrapped errors can remove important context.
- Goroutines continue until they return. The runtime does not provide structured task ownership by default.
- Context cancellation is cooperative. Code must observe the context.
- Sending to a closed channel panics. Receiving from a closed channel returns the zero value after buffered values.
- A nil channel blocks forever. A nil map supports reads but panics on writes.
- An interface can be non-nil while it contains a typed nil value.
- `defer` calls run in last-in, first-out order when the function returns or panics.
- Maps are not safe for unsynchronized concurrent writes.
- A data race can corrupt composite values even when tests appear stable.
- Package initialization runs before dependent package use and can hide startup effects.

Review goroutine lifetime, channel ownership, context propagation, nil interfaces, error wrapping, and race protection.

## Java and Kotlin

- Objects use reference semantics and garbage collection. External resources still need explicit cleanup.
- Java checked exceptions are part of the declared contract. Runtime exceptions are not.
- Kotlin null-safety weakens at Java interoperation and platform types.
- Equality can mean identity or value equality. Collection behavior depends on a correct equality and hash contract.
- Class initialization and static initialization can run code before normal object use.
- Futures and coroutines need explicit ownership, cancellation, and exception handling.
- Thread interruption and coroutine cancellation are cooperative at many boundaries.
- Shared mutable state still needs synchronization or confinement.
- Kotlin coroutines can outlive a caller when code uses an unstructured scope.
- Serialization and reflection can bypass constructor or type assumptions.

Review resource cleanup, nullability boundaries, equality contracts, task scopes, cancellation, and initialization effects.

## C#

- Objects normally use reference semantics. Value types copy unless code passes them by reference.
- Nullable reference annotations are compile-time analysis. They do not enforce runtime non-null values.
- An `async` method normally returns a hot `Task` after invocation starts its synchronous prefix.
- Cancellation is cooperative through a token. It does not roll back completed effects.
- `IDisposable` and `IAsyncDisposable` define explicit cleanup ownership.
- LINQ queries can use deferred execution and can repeat effects or observe changed state.
- Exceptions can cross async boundaries through the returned task.
- Equality, records, and mutable members can affect dictionary and set behavior.
- Static constructors and dependency injection registration can hide startup order.
- Entity Framework queries and transactions depend on provider translation and database behavior.

Review task ownership, cancellation, disposal, deferred queries, nullable boundaries, and provider-specific persistence behavior.

## C and C++

- Undefined behavior removes normal reasoning guarantees.
- C requires explicit ownership and lifetime conventions.
- C++ RAII ties cleanup to object lifetime, but raw pointers and moved objects still need clear contracts.
- References, pointers, iterators, and views can outlive their source.
- Signed overflow is undefined in C and C++. Unsigned overflow wraps.
- Data races cause undefined behavior in C++.
- Exceptions and `noexcept` affect cleanup and termination behavior.
- Copy, move, and destructor behavior can hide costs and side effects.
- Macro expansion and conditional compilation can create target-specific behavior.
- ABI, alignment, aliasing, and compiler flags can change correctness.

Review lifetime, bounds, aliasing, integer behavior, cleanup, exception guarantees, synchronization, and build configuration.

## PHP

- Scalar coercion depends on declarations, the caller file's `strict_types` setting, and the PHP version.
- Arrays are ordered maps with copy-on-write behavior, not one fixed list type.
- Loose comparison can coerce values. Identity comparison also checks the type.
- Request-scoped execution does not remove shared database, cache, queue, or worker state.
- Exceptions and errors have version-specific behavior and can leave earlier effects complete.
- References and object handles can create mutation that is not visible from a function signature.
- Autoloading and file inclusion can run top-level code.
- Long-running workers retain process state across jobs.

Review comparison operators, request versus worker lifetime, serialization, shared services, error translation, and transaction boundaries.

## Ruby

- Variables reference objects. Many core objects are mutable.
- Open classes and monkey patches can change behavior outside the local file.
- Blocks, procs, and lambdas have different return and argument behavior.
- Exceptions unwind the stack and can leave external effects complete.
- `ensure` owns cleanup that must run during normal return or exception handling.
- Method lookup depends on inheritance, included modules, prepended modules, and refinements.
- Threads share memory. Runtime implementation affects parallel execution behavior.
- Autoloading and constant lookup can create environment-specific behavior.

Review mutation, method lookup, callbacks, transaction scope, cleanup, thread safety, and framework autoload rules.

## Swift

- Value types copy by value, but copy-on-write can share storage internally.
- Classes use reference semantics and automatic reference counting.
- Strong reference cycles can retain objects until code breaks the cycle.
- Optionals represent absence. Forced unwraps move failure to runtime.
- Errors use `throw`, while traps and failed preconditions terminate normal control flow.
- Actors isolate mutable state, but suspension points permit reentrancy.
- Tasks need explicit ownership, cancellation handling, and actor boundaries.
- `Sendable` checks cross-concurrency safety but can include unchecked promises.

Review reference cycles, optional handling, actor reentrancy, task lifetime, cancellation, and main-actor ownership.

## Dart

- Dart 3 requires sound null safety. Older mixed-version programs can be unsound.
- Objects use reference semantics. Collections remain mutable unless code restricts them.
- Futures represent one asynchronous result. Streams represent multiple events and need lifecycle ownership.
- Cancellation is API-specific. A future does not provide general cancellation.
- Isolates do not share ordinary mutable memory and communicate through messages.
- `late` defers initialization checks to runtime.
- Exceptions can cross asynchronous boundaries through futures and zones.
- Flutter widget objects are immutable descriptions, while element and state objects own lifecycle.

Review null-safety boundaries, stream subscriptions, isolate messages, late initialization, async errors, and Flutter state ownership.

## Scala

- Scala combines object-oriented and functional features. Local style does not prove immutability.
- `val` prevents reassignment but does not make the referenced object immutable.
- Pattern matches can fail at runtime when cases are not exhaustive.
- Futures start when created and need an execution context.
- Exceptions inside futures become failed futures, while synchronous setup can still throw directly.
- Implicits, given instances, and extension methods can hide dependency selection.
- Lazy values defer initialization and can affect failure timing.
- Java interoperation weakens Scala-specific type and null assumptions.

Review mutability, match exhaustiveness, execution contexts, hidden implicit dependencies, lazy initialization, and Java boundaries.

## Elixir and Erlang

- Data is immutable, but processes own changing state through message loops.
- Processes do not share ordinary memory and communicate asynchronously.
- Message delivery order is guaranteed only between the same sender and receiver.
- A process mailbox can grow without a bound when consumers cannot keep pace.
- Links, monitors, supervisors, and restart strategies define failure propagation.
- Restarting a process does not roll back external effects.
- Pattern matching failures can terminate a process.
- Processes can keep stale state unless code defines refresh and version behavior.

Review supervision ownership, mailbox growth, timeout behavior, duplicate effects, restart safety, and message contracts.

## SQL and database behavior

- SQL `NULL` uses three-valued logic. Comparisons with `NULL` do not behave like normal equality.
- Row order is not guaranteed without an `ORDER BY`.
- Transaction isolation controls which concurrent states a transaction can observe.
- A transaction does not include external side effects unless the system coordinates them.
- Constraints provide stronger ownership than repeated application checks.
- Unique constraints can treat `NULL` differently across database engines.
- Time zones, collations, case rules, and numeric behavior depend on the engine and column type.
- Schema changes can lock data, rewrite tables, or behave differently across engine versions.
- ORM behavior depends on generated SQL, tracking rules, loading strategy, and transaction scope.
- Retry logic can repeat statements or external effects unless the operation is idempotent.

Review the actual database engine, schema, generated SQL, isolation level, constraints, migrations, and retry boundary.

## Official documentation

Use these sources when the repository does not pin a version or document the behavior:

- [TypeScript runtime behavior](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)
- [Rust futures](https://doc.rust-lang.org/std/future/trait.Future.html)
- [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Go specification](https://go.dev/ref/spec) and [Go memory model](https://go.dev/ref/mem)
- [Java specifications](https://docs.oracle.com/javase/specs/)
- [C# reference](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [PHP types](https://www.php.net/manual/en/language.types.declarations.php) and [PHP arrays](https://www.php.net/manual/en/language.types.array.php)
- [Dart null safety](https://dart.dev/null-safety/understanding-null-safety) and [Dart concurrency](https://dart.dev/language/concurrency)
- [Scala concurrency](https://docs.scala-lang.org/scala3/book/concurrency.html)
- [Elixir processes](https://elixir-lang.org/getting-started/processes.html)
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)

## Add a language profile

Use the same categories:

1. Type and runtime boundary.
2. Ownership and mutation.
3. Absence and invalid values.
4. Error and cleanup behavior.
5. Concurrency and cancellation.
6. Module or package initialization.
7. Build, target, and version differences.
8. Persistence and external effects.

Record stable semantics only. Put framework-specific behavior in a separate reference when it becomes large enough to need independent maintenance.
