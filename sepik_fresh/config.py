"""
config.py — Configuration Management for Sepik Fresh
Centralizes all configuration and supports environment variables
"""
import os
from datetime import timedelta

class Config:
    """Base configuration"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Session Configuration
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False').lower() == 'true'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=int(os.environ.get('SESSION_TIMEOUT', 30)))
    
    # Database Configuration
    DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_NAME = os.environ.get('DB_NAME', 'sepik_database')
    
    # Email Configuration (for future use)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@sepikfresh.pg')
    
    # Application Configuration
    ITEMS_PER_PAGE = int(os.environ.get('ITEMS_PER_PAGE', 20))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file upload
    
    # Security Configuration
    BCRYPT_LOG_ROUNDS = int(os.environ.get('BCRYPT_LOG_ROUNDS', 12))
    PASSWORD_MIN_LENGTH = int(os.environ.get('PASSWORD_MIN_LENGTH', 6))
    MAX_LOGIN_ATTEMPTS = int(os.environ.get('MAX_LOGIN_ATTEMPTS', 5))
    LOCKOUT_DURATION = int(os.environ.get('LOCKOUT_DURATION', 15))  # minutes
    
    @staticmethod
    def get_db_config():
        """Returns database configuration dictionary"""
        return {
            'host': Config.DB_HOST,
            'user': Config.DB_USER,
            'password': Config.DB_PASSWORD,
            'database': Config.DB_NAME
        }


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DB_NAME = 'sepik_database_test'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
