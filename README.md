# Lab 02 — Understand, Improve, and Deploy a Backend Service

Welcome to **Software Engineering Toolkit**.

In this lab, you will:

- Run and explore an existing FastAPI codebase.
- Document and fix a bug using the bug issue template.
- Implement a small new feature.
- Deploy the updated service to a remote Linux server using SSH, virtual environments, systemd, and Nginx.

You are **expected to use LLMs**, but:

- Run and test everything by yourself to check that it actually works.
- Ask the LLM for explanations to understand what is happening.
- Even better ask the LLM for directions on how to do each task instead of asking for a ready solution.
- The TA may ask you to explain any part of your solution.

As in the previous lab, you work on tasks **individually**, then ask a classmate to review your PRs and do the same for them.

---

## Story

You were hired by a company that develops a novel Learning Management System like Moodle.

You have joined a backend team in that company.

Your team develops a read-only service called **Course Material Service**.

The service is implemented using the FastAPI framework in Python.

Currenty, it serves course-related items (labs and tasks).

For simplicity, the backend uses data ("resources") stored is JSON files in `src/app/data/`.

A senior engineer explains your first assignment:

> Before we give you bigger features, you need to show you can:
>
> 1) Run our backend service on your machine
> 2) Verify it’s working: query the `/status` endpoint
> 3) Investigate and fix a bug in the `/items` endpoint.
> 4) Implement a missing `/outcomes` endpoint using the provided JSON resource.
> 5) Deploy your updated service to a remote Linux server.
>
> You are expected to communicate through issues and PRs, and deliver a working deployment.

### Key entities (what the API serves)

- Course tree example:

  ```console
  - [course] Software Engineering Toolkit
    - [lab] Lab 1
      - [tasks] Required tasks
        - [task] Study architecture
          - [step] Step 1
          - [step] Step 2
          ... (more steps here)
        - [task] Research market
          ... (more steps here)
    - [lab] Lab 2
      - [tasks] Tasks
        - [task] Setup
          ... (more steps here)
        - [task] Run the service
          ... (more steps here)
  ```

- `Item` is a generic node in the course tree. It has:
  - an `id` (unique string)
  - a `type` (e.g. `course`, `lab`, `tasks`, `task`, `step`)
  - optional metadata (`titles`, `descriptions`, `values`, etc.).
- An `Item` can contain nested `items`, so the structure forms a **tree**.
- The tree can potentially be of arbitrary depth so that it lets represent deeply nested subtasks.

---

## Learning outcomes

By the end of this lab, you should be able to:

- Run and modify an existing backend service locally.
- Identify and document a bug in an existing codebase.
- Apply the Git workflow (issues → branches → PRs → review) without guidance.
- Deploy a Python backend to a Linux VPS using systemd and Nginx.
- Verify that the deployed service is running and reachable externally.

---

## How the lab works

1. **Fork** this repo to your account.
2. Complete tasks in this README.
3. For each task:
   - Create/assign an **issue** using the appropriate template in `.github/ISSUE_TEMPLATE/`.
   - Implement the task on a **newly created branch**.
   - Open a **Pull Request** and request review when required.
4. After each task, show your progress to the TA, who will check it off.

---

## Tasks

Every non-trivial task must have its own GitHub issue created using the provided templates.

You work **independently**, but you will request **peer review** when required.

---

## 0. Setup

Create an issue:

- `[Task] Lab 02 setup`

Steps:

- [ ] Ensure the TA and at least one reviewing classmate have access to your repo.
- [ ] Clone the repo to your local machine.
- [ ] Install Python 3.10+ (if needed).
- [ ] Read this `README.md` once to understand the flow.

After completing, show the TA, then close the issue.

---

## PART 1 — Local development

### 1. Run the service locally

Create an issue:

- `[Task] Run the backend locally`

Steps:

- [ ] Create a virtual environment:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- [ ] Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- [ ] Run the service from `src/`:

  ```bash
  cd src
  uvicorn main:app --reload
  ```

- [ ] Open the interactive API docs: `http://127.0.0.1:8000/docs`
- [ ] Verify `/status` returns the correct JSON.
- [ ] Verify `/items/course` returns a nested “course structure” JSON.
- [ ] Document any unclear parts of the code in the issue.

TA checks: “Local app running successfully.”

---

#### Local API overview (for exploration)

Use `http://127.0.0.1:8000/docs` and try:

- `GET /status` — health check
- `GET /items/course` — full nested course structure
- `GET /items` — list items (by default: top-level; with `?type=...`: items of that type across the full nested structure)
- `GET /items/{item_id}` — fetch any item by id (including nested ones)

Tip:

- Use `/items/course` when you need the full tree.
- Use `/items` when you want a smaller response (top-level), or when you want to extract a specific `type` quickly.

### 2. Document the bug using the bug issue template

Create a **bug issue** using the template:

- `[Bug] Unexpected behavior in <endpoint/function>`

Steps:

- [ ] Focus your search on the `/items` endpoints (course structure + listing/filtering).
- [ ] Use `/items/course` to understand what items exist, then try listing with filters like `GET /items?type=lab` or `GET /items?type=task`.
- [ ] Describe the incorrect behavior.
- [ ] Add steps to reproduce it.
- [ ] Explain expected vs actual behavior.
- [ ] Add any screenshots or error logs.

This step is critical: documenting bugs is a core engineering skill.

TA checks the bug issue before you proceed.

---

### 3. Fix the bug in a PR

Create an issue:

- `[Task] Fix bug reported in <bug issue #>`

Steps:

- [ ] Create branch:

  ```bash
  git checkout -b fix/<bug-name>
  ```

- [ ] Fix the bug in code.
- [ ] Add or update a small test in `tests/`.
- [ ] Push and open a PR.
- [ ] In the PR description: `Closes #<bug-issue-number>`
- [ ] Request a review from a classmate.

After review and fixes → merge PR.

TA checks the merged PR.

---

### 4. Implement a small improvement

Create an issue:

- `[Task] Implement feature: Outcomes API (/outcomes)`

#### Background

The service includes a data file at `src/app/data/outcomes.json`, but the backend does **not** expose it yet.
If you try `/outcomes` right now, you should get a `404` until you implement the feature.

Your job is to implement an Outcomes API so the frontend (and other services) can fetch learning outcomes.

#### Requirements

- Add `GET /outcomes`
  - Returns the full outcomes payload from `src/app/data/outcomes.json`
  - Response shape: `{"outcomes": [...]}` (validated with Pydantic models)
- Add `GET /outcomes/{outcome_id}`
  - Returns one outcome by `id` (search must work for nested `suboutcomes`)
  - Returns `404` with a clear message if not found

Implementation guidance (you decide the exact structure, but keep it clean):

- Add models in `src/app/models/` (similar style to `Item`/`CourseMaterial`)
- Add a service in `src/app/services/` that loads JSON and supports lookup by id
- Add a router in `src/app/routers/` and register it in `src/main.py`

Steps:

- [ ] Create a branch.
- [ ] Implement the feature.
- [ ] Add tests for both endpoints.
- [ ] Open a PR and request review.

After proper review → merge PR.

TA checks the merged PR.

---

## PART 2 — Remote deployment (Linux VPS)

### 5. Connect to the server

Create an issue:

- `[Task] Connect to VPS`

Steps:

- [ ] SSH into the server:

  ```bash
  ssh username@SERVER_IP
  ```

- [ ] Show TA you can connect and navigate.

---

### 6. Prepare the deployment environment

Create an issue:

- `[Task] Prepare VPS environment`

Steps:

- [ ] Create directory `/var/www/myapp/`
- [ ] Upload project files (via `scp`, `rsync`, or Git pull).
- [ ] Create and activate virtualenv on server.
- [ ] Install requirements.

TA checks folder structure + venv.

---

### 7. Run the app manually on the server

Create an issue:

- `[Task] Run app manually on VPS`

Steps:

- [ ] Start (from `/var/www/myapp/src`):

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8001
  ```

- [ ] In your browser, check:

  ```text
  http://SERVER_IP:8001/status
  ```

TA checks the working endpoint.

---

### 8. Create a systemd service

Create an issue:

- `[Task] Create systemd service`

Steps:

- [ ] Create `/etc/systemd/system/myapp.service`
- [ ] Fill in the unit file for a FastAPI/Uvicorn service.
- [ ] Enable and start:

  ```bash
  sudo systemctl daemon-reload
  sudo systemctl enable myapp
  sudo systemctl start myapp
  sudo systemctl status myapp
  ```

TA checks service running.

---

### 9. Configure Nginx reverse proxy

Create an issue:

- `[Task] Configure Nginx reverse proxy`

Steps:

- [ ] Create `/etc/nginx/sites-available/myapp`
- [ ] Add reverse proxy config to `localhost:8001`
- [ ] Enable site:

  ```bash
  sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
  sudo nginx -t
  sudo systemctl reload nginx
  ```

- [ ] Visit:

  ```text
  http://SERVER_IP/status
  ```

TA checks the web response.

---

## Stretch tasks (optional)

Choose **one**:

- Add a `/version` endpoint that reads version from a file.
- Add structured logging (JSON logs).
- Add a systemd restart policy or environment variable support.
- Write a small deployment script (local → server).

---

## Repo structure

- `README.md` — story, tasks, and lab workflow.
- `src/` — the FastAPI codebase you will run and modify.
- `tests/` — unit tests for the service.
- `requirements.txt` — Python dependencies.
