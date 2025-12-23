ALTER TABLE policy_documents
ADD COLUMN llm_assumptions JSONB,
ADD COLUMN llm_unmapped_sections JSONB;
