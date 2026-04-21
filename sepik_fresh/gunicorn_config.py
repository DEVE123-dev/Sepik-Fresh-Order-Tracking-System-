"""
Gunicorn configuration file for production deployment
"""
import os

# Server socket - Render provides PORT environment variable
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"

# Worker processes - keep it simple for free tier
workers = 2
worker_class = "sync"
timeout = 120

# Logging - output to stdout/stderr for Render
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "sepik_fresh"
