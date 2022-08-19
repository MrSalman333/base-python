#! /usr/bin/env sh
set -e

# Start Uvicorn with live reload
exec uvicorn --reload --host 0.0.0.0 --port 80 --log-level info "$MODULE_NAME"