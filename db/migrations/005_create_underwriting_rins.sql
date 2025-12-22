CREATE TABLE IF NOT EXISTS underwriting_runs (
    id UUID PRIMARY KEY,
    application_id UUID NOT NULL REFERENCES applications(id),
    status TEXT NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT now(),
    completed_at TIMESTAMP
);
