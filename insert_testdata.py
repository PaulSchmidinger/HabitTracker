
from db import get_db, create_tables, add_timespan
from db import add_habit, add_check

def inizialise_db (name="main.db"):
    conn = get_db(name)
    create_tables(conn)
    add_timespan(conn, "week", 7)
    add_timespan(conn, "day", 1)

def insert_testdata_db (name="main.db"):
    conn = get_db(name)
    add_habit(conn, "test1", 1, 1)
    add_habit(conn, "test2", 2, 1)
    add_habit(conn, "test3", 1, 1)
    add_habit(conn, "test4", 2, 1)
    add_habit(conn, "test5", 1, 0)
    #4 periods
    add_check(conn, 1, 1)
    add_check(conn, 1, 1)
    add_check(conn, 1, 1)
    add_check(conn, 1, 1)
    #2 periods
    add_check(conn, 2, 0)
    add_check(conn, 2, 1)
    add_check(conn, 2, 1)
    #3 periods
    add_check(conn, 3, 1)
    add_check(conn, 3, 1)
    add_check(conn, 3, 1)
    add_check(conn, 3, 0)
    add_check(conn, 3, 1)
    add_check(conn, 3, 1)
    #5 periods
    add_check(conn, 4, 1)
    add_check(conn, 4, 1)
    add_check(conn, 4, 1)
    add_check(conn, 4, 1)
    add_check(conn, 4, 1)
    add_check(conn, 4, 0)
    #6 periods
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 0)
    add_check(conn, 5, 0)
    add_check(conn, 5, 0)
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 1)
    add_check(conn, 5, 0)


inizialise_db()
insert_testdata_db()