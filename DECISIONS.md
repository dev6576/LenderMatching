“Underwriting is async and workflow-driven”

“Frontend polls for status”

“Hatchet orchestrates lender evaluation internally”

“Rule instances and lender-specific criteria are fully data-driven and editable via the UI.
New rule types require implementing a new evaluator in code to preserve deterministic behavior, testability, and explainability. This mirrors how real-world underwriting systems balance flexibility and safety.”

“Database schema is defined via SQL migrations committed to the repository. Local setup is supported via Docker Compose for reproducibility.”