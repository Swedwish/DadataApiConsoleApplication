import sqlite3

def _print_settings_list():
    print("Settings list:\napi_token\nlanguage\nmax_count")
    
def _change_api_token(token : str, con: sqlite3.Connection, cur: sqlite3.Cursor):
    cur.execute("""UPDATE settings SET api_token = ? """, (token,))
    con.commit()
    print("Success. API token changed.")
    
def _change_language(new_language:str, con: sqlite3.Connection, cur: sqlite3.Cursor):
    if new_language not in ("ru", "en"):
        print("Incorrect language, choose 'ru' or 'en'.")
    else:
        cur.execute("""UPDATE settings SET language = ?""", (new_language,))
        con.commit()
        print("Success. Language changed.")
    
def _change_max_count(new_max_count:str, con: sqlite3.Connection, cur: sqlite3.Cursor):
    if new_max_count > 20 or new_max_count < 1:
        print(f"Invalid max_count value. Expected 1<=max_count<=20, got {new_max_count}")
    else:
        cur.execute("""UPDATE settings SET max_count = ?""", (new_max_count,))
        con.commit()
        print("Success. Max count value changed.")

def change_settings(con: sqlite3.Connection):
    cur = con.cursor()
    while True:
        print("Type a setting name you want to change and a new value, (e.g. api_token 1234567890) type '.' to go back. Type 'list' to get list of settings.")
        args = input().split()
        if len(args) != 2 and (len(args)!=1 or args[0]!='list' and args[0] !='.'):
            print(f"Error:Expected 2 arguments, got {len(args)}")
        else:
            match args[0]:
                case 'list':
                    _print_settings_list()
                case ".":
                    return
                case "api_token" | "token":
                    _change_api_token(args[1], con, cur)
                    continue
                case "language" | "lang":
                    _change_language(args[1], con, cur)
                    continue
                case "max_count":
                    try:
                        max_count = int(args[1])
                        _change_max_count(max_count, con, cur)
                    except ValueError:
                        print(f"Invalid max_count value. Expected 1<=max_count<=20, got {args[1]}")
                case _:
                    print(f"Unexpected setting name. Choose from 'api_token', 'language' or 'max_count'. Got {args[0]} instead.")