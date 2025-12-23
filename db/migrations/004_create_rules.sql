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
