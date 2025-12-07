# Lab 02 — Understand, Improve, and Deploy a Backend Service

Welcome to **Software Engineering Toolkit** 👋  

In this lab, you will:
- Run and explore an existing FastAPI codebase.
- Document and fix a bug using the bug issue template.
- Implement a small new feature.
- Deploy the updated service to a remote Linux server using SSH, virtual environments, systemd, and Nginx.

You are **expected to use LLMs**, but:
- You must understand every line of code you commit.
- You must run and test everything yourself.
- You should ask LLMs for explanations and suggestions, not full solutions.
- The TA may ask you to explain how your deployment works.

Work **independently**, but ask a classmate to review your PRs when required.

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

1. **Fork or clone** this repo to your GitHub account (or accept the Classroom assignment link).
2. Complete tasks in `LAB_STORY.md`.
3. For each task:
   - Create/assign an **issue** using the appropriate template.
   - Implement the task on a **feature branch**.
   - Open a **Pull Request** and request review when required.
4. After each task, show your progress to the TA, who will check it off.

---

## Repo structure

- `LAB_STORY.md` — narrative context and all tasks for this lab.
- `src/` — the FastAPI codebase you will run and modify.
- `.github/ISSUE_TEMPLATE/` — templates for tasks and bug reports.
- `.github/pull_request_template.md` — checklist for PR quality.

Good luck 🚀
