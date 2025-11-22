import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "DATA"
DB_PATH = DATA_DIR / "intelligent_platform.db"

def connect_database(db_path=DB_PATH):
    """Connect to SQLite database."""
    conn = sqlite3.connect(str(db_path))
    return conn