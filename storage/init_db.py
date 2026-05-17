import os
from storage.sqlite_manager import get_connection
from utils.config_loader import load_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def initialize_database():
    config = load_config()
    cluster = config["clusters"][0]
    db_path = os.path.join(BASE_DIR, cluster["storage"]["sqlite_path"])

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    connection = get_connection(db_path)
    cursor = connection.cursor()
    schema_path = os.path.join(BASE_DIR, "storage", "schema.sql")
    with open(schema_path, 'r') as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)
    connection.commit()
    connection.close()
    print(f"✅ Database initialized at: {db_path}")
if __name__ == "__main__":
    initialize_database()