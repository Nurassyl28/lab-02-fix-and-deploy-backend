# Story – Lab 02: Understand, Improve, and Deploy a Backend Service

You have joined a backend team at a growing tech startup.  
A small FastAPI service already exists. Your senior engineer gives you your first assignment:

> “Before we give you bigger features, you need to show you can:
> 1) Run our service,  
> 2) Fix a small bug,  
> 3) Add a simple improvement, and  
> 4) Deploy your change to the server.”

This is exactly how real onboarding works in many tech companies.

In this lab, you will:
- Explore and run an existing FastAPI service.
- Document and fix a bug using our bug issue template.
- Implement a small feature requested by your team.
- Deploy the service to a remote Ubuntu server using SSH, Python virtual environment, systemd, and Nginx.

Your goal is to behave like a junior engineer in a real team:
follow processes, communicate through issues and PRs, and deliver a working deployment.

---

# Tasks

> 🔁 _Every non-trivial task must have its own GitHub issue created using the provided templates in `.github/ISSUE_TEMPLATE`._

You work **independently**, but you will request **peer review** when required.

---

## 0. Setup

Create an issue:

- `[Task] Lab 02 setup`

Steps:

- [ ] Ensure the TA and at least one reviewing classmate have access to your repo.
- [ ] Clone the repo to your local machine.
- [ ] Install Python 3.10+ (if needed).
- [ ] Read this `LAB_STORY.md` once to understand the flow.

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
````

* [ ] Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
* [ ] Run the service:

  ```bash
  uvicorn main:app --reload
  ```
* [ ] Verify `/status` endpoint returns the correct JSON.
* [ ] Document any unclear parts of the code in the issue.

TA checks: “Local app running successfully.”

---

### 2. Document the bug using the bug issue template

Create a **bug issue** using the template:

* `[Bug] Unexpected behavior in <endpoint/function>`

Steps:

* [ ] Describe the incorrect behavior.
* [ ] Add steps to reproduce it.
* [ ] Explain expected vs actual behavior.
* [ ] Add any screenshots or error logs.

> 🧠 *This step is critical: documenting bugs is a core engineering skill.*

TA checks the bug issue before you proceed.

---

### 3. Fix the bug in a PR

Create an issue:

* `[Task] Fix bug reported in <bug issue #>`

Steps:

* [ ] Create branch:

  ```bash
  git checkout -b fix/<bug-name>
  ```
* [ ] Fix the bug in code.
* [ ] Add or update a small test in `tests/`.
* [ ] Push and open a PR.
* [ ] In the PR description: `Closes #<bug-issue-number>`
* [ ] Request a review from a classmate.

After review and fixes → merge PR.

TA checks the merged PR.

---

### 4. Implement a small improvement

Create an issue:

* `[Task] Implement feature: <feature name>`

The feature is specified in the repo (typically small, e.g., a `/greet?name=` endpoint, a simple counter, or input validation).

Steps:

* [ ] Create a branch.
* [ ] Implement the feature.
* [ ] Add/update tests.
* [ ] Open a PR and request review.

After proper review → merge PR.

TA checks the merged PR.

---

---

## PART 2 — Remote deployment (Linux VPS)

### 5. Connect to the server

Create an issue:

* `[Task] Connect to VPS`

Steps:

* [ ] SSH into the server:

  ```bash
  ssh username@SERVER_IP
  ```
* [ ] Show TA you can connect and navigate.

---

### 6. Prepare the deployment environment

Create an issue:

* `[Task] Prepare VPS environment`

Steps:

* [ ] Create directory `/var/www/myapp/`
* [ ] Upload project files (via `scp`, `rsync`, or Git pull).
* [ ] Create and activate virtualenv on server.
* [ ] Install requirements.

TA checks folder structure + venv.

---

### 7. Run the app manually on the server

Create an issue:

* `[Task] Run app manually on VPS`

Steps:

* [ ] Start:

  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8001
  ```
* [ ] In your browser, check:

  ```
  http://SERVER_IP:8001/status
  ```

TA checks the working endpoint.

---

### 8. Create a systemd service

Create an issue:

* `[Task] Create systemd service`

Steps:

* [ ] Create `/etc/systemd/system/myapp.service`
* [ ] Fill in the unit file (from README instructions).
* [ ] Enable and start:

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

* `[Task] Configure Nginx reverse proxy`

Steps:

* [ ] Create `/etc/nginx/sites-available/myapp`
* [ ] Add reverse proxy config to `localhost:8001`
* [ ] Enable site:

  ```bash
  sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
  sudo nginx -t
  sudo systemctl reload nginx
  ```
* [ ] Visit:

  ```
  http://SERVER_IP/
  ```

  The FastAPI root route should respond.

TA checks the web response.

---

## Stretch tasks (optional)

Choose **one**:

* Add a `/version` endpoint that reads version from a file.
* Add structured logging (JSON logs).
* Add a systemd restart policy or environment variable support.
* Write a small deployment script (local → server).

