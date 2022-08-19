#! /usr/bin/env sh
set -e

# Start Gunicorn
exec gunicorn -k "$WORKER_CLASS" "$MODULE_NAME"