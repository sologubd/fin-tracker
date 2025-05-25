uvicorn fin_tracker.main:asgi_app \
    --workers 3 \
    --host 0.0.0.0 \
    --port 8080
