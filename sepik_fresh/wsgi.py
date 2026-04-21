"""
WSGI entry point for production deployment
Use with Gunicorn: gunicorn -w 4 -b 0.0.0.0:8000 wsgi:application
"""
from app import app

# Gunicorn looks for 'application' by default
application = app

if __name__ == "__main__":
    app.run()
