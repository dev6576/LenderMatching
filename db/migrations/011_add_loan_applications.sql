CREATE TABLE loan_applications (
  id UUID PRIMARY KEY,
  submitted_at TIMESTAMP DEFAULT now(),
  application_payload JSONB NOT NULL,
  underwriting_result JSONB NOT NULL
);
