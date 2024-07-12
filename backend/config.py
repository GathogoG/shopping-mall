import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '360b1c5f493e9b6d9a1fef7c2a85d8a1b620a29c8a2f46f2a28a')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///shopping-mall.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

print("DATABASE_URI:", Config.SQLALCHEMY_DATABASE_URI)
