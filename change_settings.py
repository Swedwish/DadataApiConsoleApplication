import sqlite3

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
                    print("Settings list:\napi_token\nlanguage\nmax_count")
                case ".":
                    return
                case "api_token" | "token":
                    cur.execute("""UPDATE settings SET api_token = ? """, (args[1],))
                    con.commit()
                    print("Success. API token changed.")
                    return
                case "language" | "lang":
                    if args[1] not in ("ru", "en"):
                        print("Incorrect language, choose 'ru' or 'en'.")
                        continue
                    else:
                        cur.execute("""UPDATE settings SET language = ?""", (args[1],))
                        con.commit()
                        print("Success. Language changed.")
                        return
                case "max_count":
                    try:
                        maxCount = int(args[1])
                        if maxCount > 20 or maxCount < 1:
                            print(f"Invalid max_count value. Expected 1<=max_count<=20, got {maxCount}")
                        else:
                            cur.execute("""UPDATE settings SET max_count = ?""", (maxCount,))
                            con.commit()
                            print("Success. Max count value changed.")
                            return
                    except ValueError:
                        print(f"Invalid max_count value. Expected 1<=max_count<=20, got {maxCount}")
                case _:
                    print(f"Unexpected setting name. Choose from 'api_token', 'language' or 'max_count'. Got {args[0]} instead.")