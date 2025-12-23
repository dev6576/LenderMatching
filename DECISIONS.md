## System Architecture Decisions

### Backend-first, workflow-oriented design

The system was designed **backend-first**, with the primary focus on correctness, auditability, and explainability rather than UI completeness.

- Core underwriting logic, policy ingestion, and evaluation live entirely in the backend.
- The frontend is treated as a thin client that will eventually orchestrate and visualize backend workflows.
- This mirrors real underwriting platforms, where business logic is never UI-owned.

---

### Underwriting is async and workflow-driven

Underwriting is conceptually modeled as a **workflow**, not a synchronous request-response operation.

- Borrower application submission triggers an underwriting workflow.
- Each lender’s active policy is evaluated independently.
- Results are aggregated per application.

For the MVP, this workflow is executed synchronously, but the boundaries are explicit and migration-ready.

---

### Initial Hatchet-based design, deferred in implementation

The ingestion and underwriting flows were **originally designed to be orchestrated using Hatchet**:

- Policy ingestion
- PDF parsing
- LLM extraction
- Rule persistence
- Lender-by-lender underwriting evaluation

Due to local infrastructure constraints and timeboxing, the current implementation uses a **synchronous orchestration layer** that preserves workflow boundaries.

> No business logic would need to change to migrate back to Hatchet — only execution semantics.

---

### Frontend polls for status (future)

The intended frontend interaction model is:

- Frontend submits a request (policy ingestion or underwriting)
- Backend returns a workflow/application ID
- Frontend polls for status and results

For the MVP, results are returned synchronously to simplify evaluation and testing.

---

## Policy & Rule Modeling Decisions

### Policies are versioned and explicitly approved

- Each lender can have multiple policies over time.
- Only **one active policy per lender** is allowed.
- All newly ingested policies are created as **inactive drafts**.
- Human approval is required before a policy becomes active.

This prevents silent rule changes and enables full auditability.

---

### Rule extraction is LLM-assisted, not LLM-authoritative

For the MVP:

- Entire policy documents are extracted as raw text.
- The full text is passed to an LLM to propose draft underwriting rules.
- Extracted rules are persisted as **inactive**.
- Human review and approval (and possible modification) is required.

This avoids giving the LLM decision-making authority while still accelerating rule authoring.

---

### Deterministic rule evaluation (no LLM at decision time)

Underwriting decisions are **fully deterministic**:

- Rules are evaluated using explicit operators (>=, <=, etc.).
- Hard rules cause rejection.
- Soft rules produce warnings.
- No LLM is involved in eligibility determination.

This ensures:
- Predictability
- Testability
- Explainability
- Regulatory alignment

---

### Rule instances are data-driven; rule types are code-defined

- Individual rule instances (values, operators, hard/soft) are stored in the database.
- Lender-specific criteria are fully data-driven and intended to be editable via the UI.
- **New rule types require implementing a new evaluator in code**.

This mirrors real-world underwriting systems:
- Flexibility at the data layer
- Safety and determinism at the code layer

---

## Explainability Decisions

### Two-layer explainability

1. **Deterministic explanation**
   - Per-rule pass/fail logging
   - Hard vs soft failure separation

2. **LLM-generated narrative explanation**
   - Converts structured results into human-readable reasoning
   - Used only for explanation, never for decisions

This ensures explanations are consistent with actual logic.

---

## Data & Persistence Decisions

### PostgreSQL with explicit schema control

- PostgreSQL is used as the system of record.
- Rule values are stored as JSONB to support extensibility.
- Policy documents, rules, applications, and results are persisted.

### SQL migrations committed to the repository

- Database schema is defined via SQL migrations.
- Migrations are committed to the repo for traceability.
- Local setup is supported via Docker / Docker Compose for reproducibility.

---

## Frontend Decisions

### Frontend is illustrative, not authoritative (MVP)

- UI scaffolding exists for borrowers and lenders.
- Not all flows are fully wired to backend APIs.
- UI does not currently support rule editing.

This was a deliberate choice to prioritize backend correctness and clarity.

---

## Explicit Trade-offs Made

- Async workflows designed but executed synchronously
- LLM used for acceleration, not authority
- No authentication to reduce scope
- No UI rule editor in MVP
- No lender ranking or pricing logic

These trade-offs were made to deliver a **coherent, reviewable MVP** within time constraints.

---

## Intended Evolution

If extended further, the system would naturally evolve to include:

- Hatchet-based async orchestration
- Deterministic + hybrid rule extraction pipeline
- Full frontend-backend integration
- Rule editing and approval UI
- Authentication and role-based access
- Lender scoring and ranking

---

## Closing Note

This system is intentionally designed to resemble **real underwriting platforms**:
- conservative
- auditable
- human-in-the-loop
- deterministic at its core

Every major decision was made to balance flexibility, safety, and explainability.
