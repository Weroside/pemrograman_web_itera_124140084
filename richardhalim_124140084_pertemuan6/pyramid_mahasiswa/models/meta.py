import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def database_url():
    # Gunakan URL PostgreSQL dari lingkungan.
    return os.environ["DATABASE_URL"]


def buat_engine():
    return create_engine(database_url(), pool_pre_ping=True)
