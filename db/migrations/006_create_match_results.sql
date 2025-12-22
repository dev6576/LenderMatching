CREATE TABLE IF NOT EXISTS match_results (
    id UUID PRIMARY KEY,
    run_id UUID NOT NULL REFERENCES underwriting_runs(id),
    lender_id UUID NOT NULL REFERENCES lenders(id),
    eligible BOOLEAN NOT NULL,
    fit_score INT,
    program TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT now()
);
