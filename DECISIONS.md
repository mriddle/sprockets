# Project Decisions Log

A running log of key decisions made during development. Each entry should briefly state:
- **Problem:** What was the challenge or need?
- **Options considered:** What alternatives did I look at?
- **Decision & rationale:** What did I choose and why?

---

## Guidelines for this Log

- Only document decisions that may be revisited or are important for project history and architecture.
- If a decision was made for fun, experimentation, or learning, note it—this helps future me (us?) confidently reconsider if needed.
- For further detail, refer to the pull request or commit associated with the implementation.
- Don’t worry about every tiny choice; focus on decisions that provide context for future reassessment.

---

## 1. Monorepo Strucutre
- **Problem:** How to organize both backend and iOS app in a single repository.
- **Options considered:** Monorepo vs. separate repos for backend and iOS.
- **Decision & rationale:** Chose a monorepo for easier cross-project coordination and shared documentation.

### 2. Use of Docker and Docker Compose
- **Problem:** How to ensure consistent backend deployment across macOS and Raspberry Pi.
- **Options considered:** Native Python, Docker, Docker Compose.
- **Decision & rationale:** Chose Docker Compose for portability, reproducibility, and easy multi-service orchestration.

## 3. Use Orbstack over Docker Desktop
- **Problem:** Need a fast, resource-efficient container solution on macOS (Apple Silicon).
- **Options considered:** Docker Desktop, Orbstack
- **Decision & rationale:** Chose Orbstack for faster startup and better Apple Silicon support. Docker Desktop has been my default, but I want to try something more modern.

## 4. Use FastAPI for the backend
- **Problem:** Need a modern Python web framework for the backend API.
- **Options considered:** Flask, FastAPI, Django
- **Decision & rationale:** Chose FastAPI to try something new and for its async support. Flask is more widely adopted and lightweight, but I wanted to experiment. Django is too heavyweight for this project, and I'm already familiar with it.

### 5. Use uv for Python dependency management
- **Problem:** Need a fast, simple way to manage Python dependencies and virtual environments.
- **Options considered:** pip, poetry, uv
- **Decision & rationale:** Chose uv as it's fast, simple, and gaining popularity. Will revisit if it doesn't meet my needs.
