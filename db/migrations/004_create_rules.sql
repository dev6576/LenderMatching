CREATE TABLE IF NOT EXISTS rules (
    id UUID PRIMARY KEY,
    policy_id UUID NOT NULL REFERENCES policies(id),
    rule_type TEXT NOT NULL,
    operator TEXT NOT NULL,
    value JSONB NOT NULL,
    hard_rule BOOLEAN NOT NULL,
    weight INT,
    created_at TIMESTAMP NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS underwriting_runs (
    id UUID PRIMARY KEY,
    application_id UUID NOT NULL REFERENCES applications(id),
    status TEXT NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT now(),
    completed_at TIMESTAMP
);
