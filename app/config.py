import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_secret_key'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') or '1704d9f98f1045e5a9afb0a9d19473cb'
