lender-matching-platform/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── applications.py
│   │   │   ├── lenders.py
│   │   │   ├── policies.py
│   │   │   ├── underwriting.py
│   │   │   └── results.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── logging.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── application.py
│   │   │   ├── borrower.py
│   │   │   ├── guarantor.py
│   │   │   ├── loan.py
│   │   │   ├── lender.py
│   │   │   ├── policy.py
│   │   │   └── match_result.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── application.py
│   │   │   ├── policy.py
│   │   │   ├── underwriting.py
│   │   │   └── match_result.py
│   │   │
│   │   ├── services/
│   │   │   ├── underwriting_service.py
│   │   │   ├── matching_engine.py
│   │   │   ├── scoring.py
│   │   │   └── explanation_builder.py
│   │   │
│   │   ├── rules/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── fico.py
│   │   │   ├── paynet.py
│   │   │   ├── time_in_business.py
│   │   │   ├── geography.py
│   │   │   └── equipment.py
│   │   │
│   │   ├── pdf_ingestion/
│   │   │   ├── __init__.py
│   │   │   ├── extractor.py
│   │   │   ├── sectionizer.py
│   │   │   ├── mapper.py
│   │   │   └── validator.py
│   │   │
│   │   └── utils/
│   │       └── enums.py
│   │
│   ├── tests/
│   │   ├── test_rules.py
│   │   ├── test_matching_engine.py
│   │   └── test_scoring.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── LoanApplication.tsx
│   │   │   ├── EligibilityResults.tsx
│   │   │   └── LenderPolicies.tsx
│   │   │
│   │   ├── components/
│   │   │   ├── ApplicationForm.tsx
│   │   │   ├── MatchCard.tsx
│   │   │   └── PolicyEditor.tsx
│   │   │
│   │   ├── api/
│   │   │   └── client.ts
│   │   │
│   │   ├── types/
│   │   │   └── index.ts
│   │   │
│   │   └── App.tsx
│   │
│   └── package.json
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DECISIONS.md
│   └── API.md
│
├── README.md
└── docker-compose.yml


“Database schema is defined via SQL migrations committed to the repository. Local setup is supported via Docker Compose for reproducibility.”

docker compose up -d
python -m hatchet.server