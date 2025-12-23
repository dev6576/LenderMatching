“Underwriting is async and workflow-driven”

“Frontend polls for status”

“Hatchet orchestrates lender evaluation internally”

“Rule instances and lender-specific criteria are fully data-driven and editable via the UI.
New rule types require implementing a new evaluator in code to preserve deterministic behavior, testability, and explainability. This mirrors how real-world underwriting systems balance flexibility and safety.”

“Database schema is defined via SQL migrations committed to the repository. Local setup is supported via Docker Compose for reproducibility.”

“For the MVP, policy documents are fully extracted and passed to an LLM to propose draft underwriting rules. All extracted rules are persisted as inactive and require human validation before activation.”

“I initially designed the ingestion as a workflow-based async system. Due to local infra constraints and timeboxing, I implemented a synchronous orchestration layer with clear workflow boundaries, which can be migrated to Hatchet without business-logic changes.”