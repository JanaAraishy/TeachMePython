import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

Database_URL = os.getenv("Database")

# ------------------------------------------------
# SAVE CHAT
# ------------------------------------------------

def save_chat(user_id, question, answer):

    try:

        conn = psycopg2.connect(Database_URL)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                question TEXT,
                answer TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)

        query = """
        INSERT INTO history (user_id, question, answer)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (user_id, question, answer))

        conn.commit()

        cursor.close()
        conn.close()

        print("Saved to History")

    except Exception as e:
        print("Database error:", e)


# ------------------------------------------------
# SAVE USER
# ------------------------------------------------

def save_user(name, level):

    try:

        conn = psycopg2.connect(Database_URL)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    level INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
        """)

        query = """
        INSERT INTO users (name, level)
        VALUES (%s, %s)
        ON CONFLICT (name)
        DO UPDATE SET level = EXCLUDED.level
        RETURNING id;
        """

        cursor.execute(query, (name, level))
        user_id = cursor.fetchone()[0]

        conn.commit()
        cursor.close()
        conn.close()

        return user_id

    except Exception as e:
        raise Exception(f"Database error: {e}")