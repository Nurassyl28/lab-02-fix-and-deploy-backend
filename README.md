# Lab 02 — Understand, Improve, and Deploy a Backend Service

Welcome to **Software Engineering Toolkit**.

In this lab, you will:

- Run and explore an existing FastAPI codebase.
- Document and fix a bug using the bug issue template.
- Deploy the fixed service to a remote Linux server.

You are **expected to use LLMs**, but:

- Run and test everything by yourself to check that it actually works.
- Ask the LLM for explanations to understand what is happening.
- Even better, ask the LLM for directions on how to do each task instead of a ready solution.
- The TA may ask you to explain any part of your solution.

As in the previous lab, you work on tasks **individually**, then review each other's PRs with a classmate.

---

## Story

You were hired by a company that develops a novel e-learning system to recommend educational resources to students.

You have joined a backend team in that company.

Your team is working on a read-only service called **Course Material Service**.

The service is implemented using the FastAPI framework in Python.

Currently, it serves course-related items (labs and tasks).

For simplicity, the backend uses data stored is JSON files ("JSON resources") in `src/app/data/`.

A senior engineer explains your first assignment:

> Before we give you bigger features, you need to show you can:
>
> 1) Run our backend service on your machine
> 2) Verify it’s working: query the `/status` endpoint
> 3) Investigate and fix a bug in the `/items` endpoint.
> 4) Deploy your updated service to a remote Linux server.
>
> You are expected to communicate through issues and PRs, and deliver a working deployment.

---

## Learning outcomes for this lab

By the end of this lab, you should be able to:

- Run and modify an existing backend service locally.
- Identify and document a bug in an existing codebase.
- Apply the Git workflow (issues → branches → PRs → review) without guidance.
- Deploy a Python backend to a Linux VPS using systemd and Nginx.
- Verify that the deployed service is running and reachable externally.

---

## Lab setup

### Set up a fork

- Fork this repo;
- Clone the forked repo to your machine;
- Enable `Issues`;
- (Optional) Create a label `task` for your issues;
- (Optional) Protect your `main` branch;

See the details in [Set up a fork](https://github.com/inno-se-toolkit/lab-01-market-product-and-git#set-up-a-fork).

### Add a classmate as a collaborator

- Add a classmate as a collaborator to your fork.

See the details in [Add a classmate as a collaborator](https://github.com/inno-se-toolkit/lab-01-market-product-and-git#add-a-classmate-as-a-collaborator).

### Set up your local tools

- Set up `git` and `VS Code`.

See the details in [Set up your local tools](https://github.com/inno-se-toolkit/lab-01-market-product-and-git#set-up-your-local-tools).

### Open the repository on your machine

- Clone *your forked repo*;
- Open the cloned repo in `VS Code`.

See the details in [Open the repository on your machine](https://github.com/inno-se-toolkit/lab-01-market-product-and-git?tab=readme-ov-file#open-the-repository-on-your-machine).

### Set up `VS Code` extensions

- Install and set up recommended extensions.

See the details in [Set up `VS Code` extensions](https://github.com/inno-se-toolkit/lab-01-market-product-and-git?tab=readme-ov-file#set-up-vs-code-extensions).

## Procedure for each task

The procedure is the same for this lab as for the previous lab.

See the details in [Procedure for each task](https://github.com/inno-se-toolkit/lab-01-market-product-and-git#procedure-for-each-task).

---

## Tasks

## PART 1 — Local development

### Task 1. Run the service locally

Create an issue:

- `[Task] Run the backend locally`

Steps:

- [ ] Install Python 3.10+.

TODO: add link to how to install Python.

- [ ] Create a virtual environment:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- [ ] Install dependencies:

TODO: replace with UV.
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
- [ ] Verify `GET /items` returns a list with the course structure.
- [ ] Run the tests to check the health of the codebase:

  ```bash
  cd src
  PYTHONPATH=. pytest ../tests -v
  ```

- [ ] Notice that **one test fails**. This indicates a bug in the code that you will investigate and fix later.
- [ ] Document any unclear parts of the code in the issue.

---

#### Local API overview (for exploration)

Use `http://127.0.0.1:8000/docs` and try:

- `GET /status` — health check
- `GET /items` — list all courses
- `GET /items/{item_id}` — fetch any item by id (searches the entire tree)

Example: `GET /items/software_engineering_toolkit` returns the material for our course. Inside the course tree something like this:

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
  - [Course] MA I
   - [lab] Lab 1
   ... (more labs here)
  ```

Every course, lab, and task follow the `Item` model:

- `Item` is a generic node in the course tree. It has:
  - an `id` (unique string)
  - a `type` (e.g. `course`, `lab`, `tasks`, `task`, `step`)
  - optional metadata (`titles`, `descriptions`, `values`, etc.).
- An `Item` can contain nested `items`, so the structure forms a **tree**.
- The tree can potentially be of arbitrary depth so that it lets represent deeply nested tasks and steps.

---

### Task 2. Document the bug using the bug issue template

Create a **bug issue** using the template:

- `[Bug] Unexpected behavior in <endpoint/function>`

Steps:

- [ ] Start from the **failing test** you discovered in the previous task.
- [ ] Read the test code in [`tests/test_items.py`](./tests/test_items.py) to understand what it expects.
- [ ] Try the failing endpoint manually via the API docs to confirm the bug.
- [ ] Investigate the relevant code in `src/app/` to understand what's going wrong.
- [ ] In the bug issue:
  - [ ] Describe the incorrect behavior.
  - [ ] Add steps to reproduce it.
  - [ ] Explain expected vs actual behavior.
  - [ ] Add any screenshots or error logs.

This step is critical: documenting bugs is a core engineering skill.

TA checks the bug issue before you proceed.

---

### Task 3. Fix the bug in a PR

Create an issue:

- `[Task] Fix bug reported in <bug issue #>`

Steps:

- [ ] Create branch:

  ```bash
  git checkout -b fix/<bug-name>
  ```

- [ ] Fix the bug in code.
- [ ] Run the tests again to verify the fix:

  ```bash
  cd src
  PYTHONPATH=. pytest ../tests -v
  ```

- [ ] All tests should now pass.
- [ ] Push and open a PR.
- [ ] In the PR description: `Closes #<bug-issue-number>`
- [ ] Request a review from a classmate.

After review and fixes → merge PR.

TA checks the merged PR.

---


## PART 2 — Remote deployment (Linux VPS)

### Task 4. Connect to the server

Create an issue:

- `[Task] Connect to VPS`

Steps:

- [ ] SSH into the server:

  ```bash
  ssh username@SERVER_IP
  ```

- [ ] Show TA you can connect and navigate.

---

### Task 5. Prepare the deployment environment

Create an issue:

- `[Task] Prepare VPS environment`

Steps:

- [ ] Create directory `/var/www/myapp/`
- [ ] Upload project files (via `scp`, `rsync`, or Git pull).
- [ ] Create and activate virtualenv on server.
- [ ] Install requirements.

TA checks folder structure + venv.

---

### Task 6. Run the app manually on the server

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

### Task 7. Create a systemd service

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

### Task 8. Configure Nginx reverse proxy

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



### Task 10. Implement Learning outcomes (`/outcomes` endpoint)

Outcomes are knowledge and skills that a student is expected to acquire as a result of completing a lab.

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

- Add models in `src/app/models/` (similar style to `Item`)
- Add a service in `src/app/services/` that loads JSON and supports lookup by id
- Add a router in `src/app/routers/` and register it in `src/main.py`

Steps:

- [ ] Create a branch.
- [ ] Implement the feature.
- [ ] Add tests for both endpoints.
- [ ] Open a PR and request review.

After proper review → merge PR.

TA checks the merged PR, that the new endpoint serves the correct data, tests are implemented and run correctly."

---

### Task 11. TODO: make the task proper.
- Add a systemd restart policy or environment variable support.

### Task 12. TODO: add a task to update docker compose in some smart way.

---

## Repo structure

- `README.md` — story, tasks, and lab workflow.
- `src/` — the FastAPI codebase you will run and modify.
- `tests/` — unit tests for the service.
- `requirements.txt` — Python dependencies.
