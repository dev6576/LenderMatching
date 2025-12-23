CREATE TABLE policy_documents (
    id UUID PRIMARY KEY,
    lender_id UUID NOT NULL,
    policy_id UUID,
    filename TEXT NOT NULL,
    content_type TEXT NOT NULL,
    raw_text TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
