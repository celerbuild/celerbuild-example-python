# Development Gunicorn Configuration File
import multiprocessing

# Number of worker processes for development
# Using minimal workers for development environment
workers = 2

# Worker class type
# Using Uvicorn's ASGI worker for FastAPI compatibility
worker_class = "uvicorn.workers.UvicornWorker"

# Binding address and port
# Allows connections from all interfaces
bind = "0.0.0.0:8084"

# Request timeout in seconds
timeout = 120

# Enable auto-reload for development
# Automatically restart workers when code changes
reload = True

# Logging configuration
# "-" means stdout/stderr for development ease
accesslog = "-"
errorlog = "-"
# More verbose logging for development
loglevel = "debug"