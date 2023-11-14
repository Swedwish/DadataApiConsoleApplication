from dadata import Dadata
import sqlite3
from httpx import HTTPStatusError

def request(con: sqlite3.Connection,*args):
    cur = con.cursor()
    token = cur.execute("SELECT api_token FROM settings").fetchone()[0]
    if token == '-1':
        print("You need to set your api token using settings command first.")
        return
    max_count = cur.execute("SELECT max_count FROM settings").fetchone()[0]
    lang = cur.execute("SELECT language FROM settings").fetchone()[0]
    dadata = Dadata(token)
    try:
        result = dadata.suggest(name = "address",query=" ".join(args))
    except HTTPStatusError  as e:
        match e.response.status_code:
            case 404:
                print("Error 404, api address may have been moved.")
            case 403:
                print("Error 403, please double-check your API token. Try reentering it.")
            case _:
                print(f"Error {e.response.status_code}.")
        return
    if len(result) == 0:
        print("Sorry, nothing was found for your request.")
        return
    print("Here's the list of adresses that were found for your request:")
    for index, address in enumerate(result):
        print(index , '.' , address["value"], sep='')
    print("Pick one entry for more info by typing its' number or type dot symbol ('.') to go back.")
    while True:
        answer = input()
        if answer == '.':
            return
        else:
            try:
                if int(answer) in range(len(result)):
                    result = dadata.suggest(name="address", query=result[int(answer)]['unrestricted_value'], count=max_count, language=lang)
                    print(f"""Geographical latitude of chosen location is {result[0]['data']['geo_lat']}\nGeographical longitude of chosen locantion is {result[0]['data']['geo_lon']}""")
                    break
                else:
                    print("I do not understand this input, pick one entry for more info by typing its' number or type dot symbol ('.') to go back.")
            except ValueError:
                print("I do not understand this input, pick one entry for more info by typing its' number or type dot symbol ('.') to go back.")
        