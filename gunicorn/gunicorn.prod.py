# Production Gunicorn Configuration File
import multiprocessing

# Number of worker processes
# Formula: (2 x NUM_CORES) + 1 for optimal performance
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class type
# Using Uvicorn's ASGI worker for FastAPI compatibility
worker_class = "uvicorn.workers.UvicornWorker"

# Binding address and port
# Allows connections from all interfaces
bind = "0.0.0.0:8084"

# Request timeout in seconds
# Increased for handling longer requests
timeout = 120

# Disable auto-reload in production
# Prevents unnecessary restarts and resource usage
reload = False

# Production logging configuration
# Logging to files for persistence and monitoring
accesslog = "/var/log/celerbuild/access.log"
errorlog = "/var/log/celerbuild/error.log"
# Less verbose logging for production
loglevel = "warning"

# Additional production settings
# Maximum number of requests before worker restart
max_requests = 1000
max_requests_jitter = 50

# Graceful timeout for worker shutdown
graceful_timeout = 30

# SSL configuration (if needed)
# keyfile = "/path/to/keyfile"
# certfile = "/path/to/certfile"