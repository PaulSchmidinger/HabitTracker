# PS

from db import get_db, create_tables, add_timespan


def inizialise_db(name="main.db"):
    conn = get_db(name)
    create_tables(conn)
    add_timespan(conn, "week", 7)
    add_timespan(conn, "day", 1)


inizialise_db()
