"""
config.py — Configuration de JDN AniDex (Render-ready)
"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'jdn-anidex-secret-key-2025-changez-moi')

    # Render fournit "postgres://" mais SQLAlchemy requiert "postgresql://"
    _db_url = os.environ.get('DATABASE_URL', 'sqlite:///jdn_anidex.db')
    if _db_url.startswith('postgres://'):
        _db_url = _db_url.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', 'VOTRE_CLE_API_ICI')
    ADMIN_USERNAME     = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD     = os.environ.get('ADMIN_PASSWORD', 'admin123')
    QUIZ_QUESTIONS_COUNT = 10
    PERMANENT_SESSION_LIFETIME = 3600
