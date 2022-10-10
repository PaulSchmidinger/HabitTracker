import sqlite3
from venv import create

def get_db(name="main.db"):
    db = sqlite3.connect(name)
    return db

def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Habits(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                create_d DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN NOT NULL,
                timespan INT,
                FOREIGN KEY (timespan) REFERENCES timespans (id))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Checks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
                habit_id INT,
                FOREIGN KEY (habit_id) REFERENCES Habits (id))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Timespans(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timespan TEXT)""")
    db.commit()

def add_habit(db, name, active, timespan):
    cur = db.cursor()
    cur.execute("INSERT INTO Habits VALUES (?, ?, ?)", (name, active, timespan))
    db.commit()

def add_check(db, habit_id):
    cur = db.cursor()
    cur.execute("INSERT INTO Checks VALUES (?)", (habit_id))
    db.commit()

def add_timespan (db, timespan):
    cur = db.cursor()
    cur.execute("INSERT INTO Timespans VALUES (?)", (timespan))
    db.commit()

def get_habits_data(db,id):
    cur = db.cursor()
    cur.execute("SELECT * FROM Habits WHERE id=?", (id))
    return cur.fetchall()

db = get_db()
create_tables(db)