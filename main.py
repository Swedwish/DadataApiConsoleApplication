import sqlite3

from help import help
from greetings import greetings
from exit import finish_running
from dadata_request import request
from change_settings import change_settings


def start():
    con = sqlite3.connect("settings.db")
    cur = con.cursor()
    res = cur.execute("SELECT name FROM sqlite_master").fetchall()

    if res == []:
        cur.execute(
            "CREATE TABLE settings(language TEXT, api_token TEXT, max_count INT)"
        )
        cur.execute(
            """INSERT INTO settings(language, api_token, max_count) VALUES
                    ('ru', '-1', 10)"""
        )
        con.commit()

    greetings()

    while True:
        print("Type your command:")
        command, *args = input().split()
        match command:
            case "help" | "h":
                help(*args)
            case "exit" | "e" | "q":
                finish_running(con=con)
            case "dadata" | "dd":
                request(con, *args)
            case "settings" | "s":
                change_settings(con)
            case _:
                print("Command is not recognised. Type 'help' for help.")


start()
