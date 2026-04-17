# 🚧 HirePilot (Work in Progress)

**HirePilot** is a backend application built with FastAPI designed to manage and analyze job applications.

The system helps track job offers, monitor application progress, and extract structured data from job descriptions using AI.

---

## 🎯 Purpose

This project focuses on building a **real-world backend system**, not just a CRUD app.

Key goals:

- design a **clean, scalable architecture**
- enforce strict **separation of concerns**
- implement **business logic beyond simple CRUD**
- build **testable and maintainable code**
- simulate real backend challenges (data processing, validation, async tasks)

---

## ⚙️ Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL / SQLite
- (planned) AI integration for job description parsing

---

## 🧱 Architecture

The project follows a layered architecture:

- `api/` → HTTP layer (routes, request/response handling)
- `services/` → business logic and use cases
- `repositories/` → database access layer
- `models/` → ORM models (SQLAlchemy)
- `schemas/` → data validation (Pydantic)
- `core/` → configuration, exceptions, shared logic
- `db/` → database setup and session management

---

## 🚀 MVP Scope

Initial version includes:

- creating and managing job offers
- tracking applications and statuses
- storing raw job descriptions
- basic structured data extraction (AI-assisted)
- clean service-repository flow

---

## 🔮 Planned Features

- AI-based job description parsing pipeline  
- job offer **scoring system** (match vs. candidate profile)  
- application **event history** (instead of simple status)  
- reminders for follow-ups  
- async background processing  
- basic analytics (response rate, success rate)  

---

## ⚠️ Project Philosophy

This is not a feature-heavy project.

Priority is:

> **code quality > quantity of features**

That means:

- no business logic in routes
- strict layer boundaries
- meaningful naming
- testable services

---

## 📌 Status

Early development stage.

Current focus:
- project structure
- core domain models
- first API endpoints

---

## 🧠 Why this project?

Most portfolio projects stop at CRUD.

HirePilot aims to go further by introducing:

- domain-driven thinking
- real business logic
- system design decisions
- AI integration in a controlled, testable way

---
