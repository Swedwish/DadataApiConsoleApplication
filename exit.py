import sqlite3


def finish_running(con: sqlite3.Connection):
    print("Exiting...")
    con.close()
    exit(0)
