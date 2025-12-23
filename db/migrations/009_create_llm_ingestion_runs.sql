CREATE TABLE llm_ingestion_runs (
    id UUID PRIMARY KEY,
    policy_id UUID NOT NULL,
    model TEXT NOT NULL,
    prompt_version TEXT NOT NULL,
    input_tokens INTEGER,
    output_tokens INTEGER,
    assumptions JSONB,
    unmapped_sections JSONB,
    raw_llm_output JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
