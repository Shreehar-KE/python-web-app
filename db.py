import sqlite3
import os

DB_FILE = 'notes.sqlite3'


def init_db():
    """Creates a db file if none exists and sets up a "notes" table"""
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE notes (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL)''')
        conn.commit()
        conn.close()
        print("Database initialized: notes.sqlite3")
    else:
        print("Database already exists: notes.sqlite3")


def add_note_to_db(title, content):
    """Inserts a new note into the database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()


def get_all_notes():
    """Retrieves all the notes stored in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return notes
