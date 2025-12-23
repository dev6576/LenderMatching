from sqlalchemy import Column, String, Boolean, TIMESTAMP, func, Integer, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from uuid import uuid4
import uuid

Base = declarative_base()


class Lender(Base):
    __tablename__ = "lenders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )

class LoanApplicationRecord(Base):
    __tablename__ = "loan_applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    submitted_at = Column(DateTime, server_default=func.now())

    application_payload = Column(JSONB, nullable=False)
    underwriting_result = Column(JSONB, nullable=False)

class Policy(Base):
    __tablename__ = "policies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lender_id = Column(UUID(as_uuid=True), ForeignKey("lenders.id"), nullable=False)
    program = Column(String, nullable=False)
    version = Column(Integer, nullable=False)
    active = Column(Boolean, default=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )


class Rule(Base):
    __tablename__ = "rules"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    policy_id = Column(UUID(as_uuid=True), ForeignKey("policies.id"), nullable=False)

    rule_type = Column(String, nullable=False)
    operator = Column(String, nullable=False)
    value = Column(MutableDict.as_mutable(JSONB), nullable=False)

    hard_rule = Column(Boolean, nullable=False)
    weight = Column(Integer)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )


class PolicyDocument(Base):
    __tablename__ = "policy_documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lender_id = Column(UUID(as_uuid=True), nullable=False)
    policy_id = Column(UUID(as_uuid=True), nullable=True)

    filename = Column(Text, nullable=False)
    content_type = Column(Text, nullable=False)
    raw_text = Column(Text, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

    llm_assumptions = Column(JSONB, nullable=True)
    llm_unmapped_sections = Column(JSONB, nullable=True)


class LLMIngestionRun(Base):
    __tablename__ = "llm_ingestion_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    policy_id = Column(UUID(as_uuid=True), nullable=False)

    model = Column(Text, nullable=False)
    prompt_version = Column(Text, nullable=False)

    input_tokens = Column(Integer)
    output_tokens = Column(Integer)

    assumptions = Column(JSONB)
    unmapped_sections = Column(JSONB)
    raw_llm_output = Column(JSONB)

    created_at = Column(TIMESTAMP, server_default=func.now())

