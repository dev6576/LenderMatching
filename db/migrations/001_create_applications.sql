CREATE TABLE IF NOT EXISTS applications (
    id UUID PRIMARY KEY,
    payload JSONB NOT NULL,
    status TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now()
);
