from database import cursor, conn
from datetime import datetime

def add_habit(name):
    cursor.execute("INSERT INTO habits (name) VALUES (?)", (name,))
    conn.commit()

def list_habits():
    cursor.execute("SELECT * FROM habits")
    return cursor.fetchall()

def mark_habit(habit_id):
    today = datetime.now().date()
    cursor.execute(
        "INSERT INTO records (habit_id, date, done) VALUES (?, ?, ?)",
        (habit_id, today, 1)
    )
    conn.commit()