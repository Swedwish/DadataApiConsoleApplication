import sqlite3
def finishRunning(con:sqlite3.Connection):
    print("Exiting...")
    con.close()
    exit(0)