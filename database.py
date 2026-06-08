import sqlite3
import os

DB_PATH = "ideaforge.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic  TEXT NOT NULL, 
        idea TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP )
        """
    )
    conn.commit()
    conn.close()

def save_idea(topic, idea):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ideas (topic, data) VALUES (?, ?)", (topic, idea))
    conn.commit()
    conn.close()


def get_all_ideas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ideas ORDER BY created_at DESC")
    ideas = cursor.fetchall()
    conn.close()
    return ideas

def delete_idea(idea_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ideas WHERE id = ?", (idea_id,))
    conn.commit()
    conn.close()
