CREATE TABLE IF NOT EXISTS rule_evaluations (
    id UUID PRIMARY KEY,
    match_result_id UUID NOT NULL REFERENCES match_results(id),
    rule_type TEXT NOT NULL,
    passed BOOLEAN NOT NULL,
    explanation TEXT NOT NULL
);
