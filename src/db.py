"""
Database connection module for Geopolitical Exposure Project.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

def _build_db_url() -> str:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"

def get_engine() -> Engine:
    return create_engine(_build_db_url(), pool_pre_ping=True)

def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        # Test both schemas exist
        result = conn.execute(text("SELECT current_database();")).scalar()
        geo_exists = conn.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'geo';")).scalar()
        ev_exists = conn.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ev';")).scalar()
        
        print(f"Connected to: {result}")
        print(f"Project 1 (ev schema): {'✅ Found' if ev_exists else '❌ Missing'}")
        print(f"Project 2 (geo schema): {'✅ Found' if geo_exists else '❌ Missing'}")

if __name__ == "__main__":
    test_connection()