start:
	uvicorn 'fin_tracker.main:asgi_app' \
    --host 127.0.0.1 \
    --port 5000 \
    --reload

format:
	ruff check --select I --fix
