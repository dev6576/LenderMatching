CREATE TABLE IF NOT EXISTS policies (
    id UUID PRIMARY KEY,
    lender_id UUID NOT NULL REFERENCES lenders(id),
    program TEXT NOT NULL,
    version INT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT false,
    created_at TIMESTAMP NOT NULL DEFAULT now()
);
