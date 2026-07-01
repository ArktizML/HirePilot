# 🚀 HirePilot

HirePilot is a back-end application built with FastAPI designed to manage and analyze job applications.
The system helps to track job offers, monitor application progress, and extract structured data from job descriptions using AI.

---

## 🎯 Purpose

This project focuses on building a real-world backend system.
Key goals:

- design a clean, scalable architecture
- enforce strict separation of concerns
- implement business logic
- build testable and maintainable code
- simulate real backend challenges (data processing, validation, async tasks)

---

## ⚙️ Tech Stack

- **FastAPI** — HTTP framework
- **SQLAlchemy 2.0** — ORM and database access
- **Pydantic v2** — data validation and schemas
- **SQLite** (dev) / **PostgreSQL** (planned)
- **Pytest** — testing

---

## 🧱 Architecture

The project follows a layered architecture with strict separation of concerns:

```
app/
├── api/          → HTTP layer (routes, request/response handling)
├── services/     → business logic and use cases
├── repositories/ → database access layer
├── models/       → ORM models (SQLAlchemy)
├── schemas/      → data validation (Pydantic)
├── core/         → configuration, exceptions, enums
├── db/           → database setup, session management
└── tests/        → (Pytest)
```

---

## 📡 API Endpoints

### Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/jobs/` | Get all jobs |
| GET | `/api/v1/jobs/{id}` | Get job by id |
| POST | `/api/v1/jobs/` | Create a job |
| PATCH | `/api/v1/jobs/{id}` | Update a job |
| DELETE | `/api/v1/jobs/{id}` | Delete a job |
| POST | `/api/v1/jobs/{id}/parse` | Parse job description (AI) |

### Applications
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/applications/job/{job_id}` | Get all applications for a job |
| GET | `/api/v1/applications/{id}` | Get application by id |
| POST | `/api/v1/applications/` | Create an application |
| PATCH | `/api/v1/applications/{id}` | Update an application |
| DELETE | `/api/v1/applications/{id}` | Delete an application |

---

## ▶️ Running locally

```bash
# install dependencies
pip install -r requirements.txt

# create .env file
cp .env.example .env

# start the server
uvicorn app.main:app --reload
```


---

## 🧪 Running tests

```bash
pytest -v
```

---

## 📌 Current status

✅ Done:
- layered project structure (api / services / repositories / models / schemas)
- SQLAlchemy ORM models — `Job`, `Application`
- Pydantic v2 schemas — `JobCreate`, `JobRead`, `JobUpdate`, `ApplicationCreate`, `ApplicationRead`, `ApplicationUpdate`
- `ApplicationStatus` enum
- custom exception classes with FastAPI global handlers
- full CRUD endpoints - jobs and applications
- job description parsing endpoint with mock AI (`POST /jobs/{id}/parse`)
- `parsed_data` JSON field stored in database after parsing
- database session management and initialization

🔮 Planned:
- real AI integration for job description parsing
- job offer scoring system (match vs. candidate profile)
- application event history
- async background processing
- basic analytics (response rate, success rate)
- Docker support

---

## ⚠️ Project Philosophy

This is not a feature-heavy project.
Priority is: **code quality > quantity of features**

---

## 🧠 Why this project?

Most portfolio projects stop at CRUD but not this.
HirePilot aims to go further by introducing:

- domain-driven thinking
- real business logic
- system design decisions
- AI integration in a controlled, testable way