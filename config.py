from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE_PATH = BASE_DIR / "shop.db"

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "edf79ba4a94387c24e640247930f72d8657fc5a02d791ed5943aa0956702c9fe"


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
