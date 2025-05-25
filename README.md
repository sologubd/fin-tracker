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
### Using `flask` utility
```
flask --app fin_tracker.main:app run --reload
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
