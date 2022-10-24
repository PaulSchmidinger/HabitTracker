# PS

import sqlite3
import pandas as pd


def get_db(name="main.db"):
    """Connects to database and creates new database file, if not exists."""
    db = sqlite3.connect(name)
    return db


def create_tables(db):
    """Creates new database tables, if not exist."""
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Habits(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                create_d DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
                active INT,
                timespan INT,
                FOREIGN KEY (timespan) REFERENCES timespans (id))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Checks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datetime DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
                habit_id INT,
                in_time INT,
                FOREIGN KEY (habit_id) REFERENCES Habits (id))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Timespans(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timespan TEXT,
                days INT)""")
    db.commit()


def add_habit(db, name: str, timespan: int, active: int = 1):
    """Stores new habit in database."""
    cur = db.cursor()
    cur.execute("INSERT INTO Habits (name, active, timespan) VALUES (?, ?, ?)",
                (name, active, timespan))
    db.commit()


def add_check(db, habit_id: int, in_time: int):
    """Stores new check in database."""
    cur = db.cursor()
    cur.execute(
        "INSERT INTO Checks (habit_id, in_time) VALUES (?, ?)", (habit_id, in_time))
    db.commit()


def add_timespan(db, timespan: str, days: int):
    """Stores new timespan in database."""
    cur = db.cursor()
    cur.execute(
        "INSERT INTO Timespans (timespan, days) VALUES (?, ?)", (timespan, days))
    db.commit()


def __get_data(db, table):
    """Returns all content of the Habits table. For internal use only!"""
    cur = db.cursor()
    cur.execute("SELECT * FROM "+table)

    return cur.fetchall()


def get_habit_id(db, name: str):
    """Returns ID of given habit."""
    cur = db.cursor()
    cur.execute("SELECT id FROM Habits WHERE name=? AND active=1", (name,))
    id = cur.fetchone()

    try:
        return id[0]
    except:
        return "Habit not in database. Please check, if you spelled the name correctly and if the habit is active."


def get_habit_names(db, all: int = 1):
    """Returns habit names from database. Returns all habits if argument "all" is set to 1, if not, it just returns the active habits."""
    cur = db.cursor()
    if all == 1:
        cur.execute("SELECT name FROM Habits")
    else:
        cur.execute("SELECT name FROM Habits WHERE active=1")

    return cur.fetchall()


def update_deactiveate(db, id: int):
    """Set given Habit inactive."""
    cur = db.cursor()
    cur.execute("UPDATE Habits SET active=0 WHERE id=?", (id,))
    db.commit()


def get_timespan_id(db, timespan: str):
    """Returns ID of given timespan."""
    cur = db.cursor()
    cur.execute("SELECT id FROM Timespans WHERE timespan=?", (timespan,))
    id = cur.fetchone()

    try:
        return id[0]
    except:
        raise Exception("Timespan not in database!")


def get_habits_timespan(db, id: int):
    """Returns timespan of the given habit."""
    cur = db.cursor()
    cur.execute("SELECT Timespans.timespan, Timespans.days FROM Timespans JOIN Habits ON Timespans.id = Habits.timespan WHERE Habits.id=?", (id,))
    timespan = cur.fetchone()
    timespan_name = timespan[0]
    timespan_days = timespan[1]

    return timespan_name, timespan_days


def get_habits_checks(db, id: int):
    """Returns the Checks of a given habit."""
    cur = db.cursor()
    cur.execute("SELECT datetime, in_time FROM Checks WHERE habit_id=?", (id,))

    return cur.fetchall()


def get_streaks(db, id: int):
    """Returns the Streaks of a given habit."""
    cur = db.cursor()
    cur.execute("SELECT in_time FROM Checks WHERE habit_id=?", (id,))

    return cur.fetchall()


def get_habits(db, all: int = 1, timespan: str = "all"):
    """Returns all habits from database. Returns all habits if argument "all" is set to 1, if not, it just returns the active habits."""
    cur = db.cursor()
    if timespan == "all":
        if all == 1:
            cur.execute(
                "SELECT Habits.name, Habits.create_d, Timespans.timespan, Habits.active FROM Timespans JOIN Habits ON Timespans.id = Habits.timespan")
        else:
            cur.execute(
                "SELECT Habits.name, Habits.create_d, Timespans.timespan FROM Timespans JOIN Habits ON Timespans.id = Habits.timespan WHERE Habits.active=1")
    else:
        if all == 1:
            cur.execute("SELECT Habits.name, Habits.create_d, Timespans.timespan, Habits.active FROM Timespans JOIN Habits ON Timespans.id = Habits.timespan WHERE Timespans.timespan=?", (timespan,))
        else:
            cur.execute("SELECT Habits.name, Habits.create_d, Timespans.timespan FROM Timespans JOIN Habits ON Timespans.id = Habits.timespan WHERE Habits.active=1 AND Timespans.timespan=?", (timespan,))

    return cur.fetchall()


def get_timespans(db):
    """Returns all defined timespans."""
    cur = db.cursor()
    cur.execute("SELECT timespan, days FROM Timespans")

    return cur.fetchall()


def get_streak_data(db, timespan: str = "all", habitname: str = "all"):
    """Return the streaks of all habits each with the same periodicity or for a given habit. If you ask for a habit, it has to be active. Returns pandas DataFrame."""

    cur = db.cursor()

    if timespan == "all" and habitname != "all":
        cur.execute("SELECT Habits.name, Checks.datetime, Checks.in_time FROM Checks JOIN Habits ON Checks.habit_id = Habits.id WHERE Habits.active=1 AND Habits.name=?", (habitname,))
    elif timespan != "all" and habitname == "all":
        cur.execute("SELECT Habits.name, Checks.datetime, Checks.in_time FROM Checks JOIN Habits ON Checks.habit_id = Habits.id JOIN Timespans ON Timespans.id = Habits.timespan WHERE Timespans.timespan=?", (timespan,))

    df_streak_data = pd.DataFrame(cur.fetchall(), columns=[
                                  "Habitname", "Time_checked", "in_time"])

    return df_streak_data
