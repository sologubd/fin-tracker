# Manage Dependencies

- [uv](https://docs.astral.sh/uv/concepts/projects/dependencies/)

# Start the app
## Create visrtual environment

```
uv venv
uv sync
source .venv/bin/activate
```

## Start application
### Using `uvicorn`
```
uvicorn fin_tracker.main:asgi_app \
    --host 127.0.0.1 \
    --port 5000 \
    --reload
```
### Using `Makefile` utility
```
make start
```
### With uvicorn
```
bash ./start.sh
```

# Development
## Run formatter
```
make format
```
