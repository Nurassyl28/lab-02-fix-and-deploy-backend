# Lab 02 proof

Use this file to collect evidence for TA checks (commands you ran + outputs / screenshots).

## Local run

- Status endpoint: `GET /status` returns `{"status": "ok"}`
- Items endpoint: `GET /items/lab-02-run-local` originally returned 404.
- Failing test output:

```
tests/test_items.py::test_get_item_by_id FAILED
E       assert 404 == 200
E        +  where 404 = <Response [404 Not Found]>.status_code
```

## Bug investigation

- Summary: The endpoint `/items/{item_id}` returned 404 for existing items (like `lab-02-run-local`).
- Cause: The function `find_item_by_id` in `item_service.py` was comparing the requested `item_id` against `item.type` instead of `item.id`.
- Fix: Changed `item.type == item_id` to `item.id == item_id`.
- Verification (tests passed):

```
tests/test_items.py::test_get_course_by_id PASSED
tests/test_items.py::test_list_items PASSED
tests/test_items.py::test_get_item_by_id PASSED
tests/test_status.py::test_status PASSED
```

## Deployment (Docker Compose)

- Docker + Compose versions: `Docker version 28.2.2`, `Docker Compose version v2.37.1`
- `docker compose up` output:
```
[+] Running 4/4
 ✔ app                      Built
 ✔ Network myapp_default    Created
 ✔ Container myapp-app-1    Started
 ✔ Container myapp-nginx-1  Started
```
- `docker compose ps` output:
```
NAME            IMAGE               COMMAND                  SERVICE  STATUS   PORTS
myapp-app-1     myapp-app           "uv run uvicorn src.…"   app      Up       8000/tcp
myapp-nginx-1   nginx:1.27-alpine   "/docker-entrypoint.…"   nginx    Up       0.0.0.0:80->80/tcp
```

## Nginx

- `nginx -t` output (inside container):
```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

## Debug logs

- `docker compose logs` output:
```
app-1  | INFO:     Started server process [1]
app-1  | INFO:     Uvicorn running on http://0.0.0.0:8000
nginx-1  | /docker-entrypoint.sh: Configuration complete; ready for start up
```


## Stretch Goal: Task 10 (Outcomes API + HTTPS)

- Implementation: Added `src/app/models/outcome.py`, `service`, `router`.
- Tests: `tests/test_outcomes.py` passed.
- Deployment: Replaced Nginx with **Caddy** for automatic HTTPS.
- HTTPS Verification: Application is accessible at `https://46.224.249.95.nip.io/docs`.
