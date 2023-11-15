import sqlite3

from httpx import HTTPStatusError
from dadata import Dadata

def _handle_http_error(e):
    match e.response.status_code:
        case 404:
            print("Error 404, api address may have been moved.")
        case 403:
            print("Error 403, please double-check your API token. Try reentering it.")
        case _:
            print(f"Error {e.response.status_code}.")
            
def _choose_one_option(dadata:Dadata, max_count:int, language: str, location_list):
    while True:
        answer = input()
        if answer == '.':
            return
        else:
            try:
                if int(answer) in range(len(location_list)):
                    result = dadata.suggest(name="address", query=location_list[int(answer)]['unrestricted_value'], count=max_count, language=language)
                    if result[0]['data']['geo_lat'] == None:
                        print("Sorry, no geographical coordinates are availible for chosen address.")
                    else:
                        print(f"""Geographical latitude of chosen location is {result[0]['data']['geo_lat']}\nGeographical longitude of chosen locantion is {result[0]['data']['geo_lon']}""")
                    break
                else:
                    print("I do not understand this input, pick one entry for more info by typing its' number or type dot symbol ('.') to go back.")
            except ValueError:
                print("I do not understand this input, pick one entry for more info by typing its' number or type dot symbol ('.') to go back.")

def request(con: sqlite3.Connection,*args):
    cur = con.cursor()
    token = cur.execute("SELECT api_token FROM settings").fetchone()[0]
    max_count = cur.execute("SELECT max_count FROM settings").fetchone()[0]
    language = cur.execute("SELECT language FROM settings").fetchone()[0]
    dadata = Dadata(token)
    
    if token == '-1':
        print("You need to set your api token using settings command first.")
        return
    
    try:
        result = dadata.suggest(name = "address",query=" ".join(args), count=max_count, language=language)
    except HTTPStatusError  as e:
        _handle_http_error(e)
        return
    
    if len(result) == 0:
        print("Sorry, nothing was found for your request.")
        return
    
    print("Here's the list of adresses that were found for your request:")
    
    for index, address in enumerate(result):
        print(index , '.' , address["value"], sep='')
        
    print("Pick one entry for more info by typing its' number or type dot symbol ('.') to go back.")
    _choose_one_option(dadata, max_count, language, result)
    
        