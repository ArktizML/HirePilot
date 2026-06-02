# Contributing to HirePilot

## Setup

```bash
# clone the repository
git clone https://github.com/ArktizML/HirePilot.git
cd HirePilot

# create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# install dependencies
pip install -r requirements.txt

# create .env file
cp .env.example .env
```

## Running the app

```bash
uvicorn app.main:app --reload
```

API docs: http://127.0.0.1:8000/docs

## Running tests

```bash
pytest -v
```

## Project structure

```
app/
├── api/          → routes and endpoints
├── services/     → business logic
├── repositories/ → database queries
├── models/       → SQLAlchemy ORM models
├── schemas/      → Pydantic schemas
├── core/         → config, exceptions, enums
├── db/           → session and initialization
└── tests/        → pytest test suite
```

## Code style

- follow existing layered architecture — no business logic in endpoints, no DB queries in services
- every new endpoint needs a corresponding test
- use custom exceptions from `core/exceptions.py` instead of raising HTTP errors directly