def help(*args):
    if len(args) > 1:
        print(f"Too many args. Expected 0 or 1, got {len(args)}")
        return
    elif len(args) == 0:
        print("Type help command (e.g. help dd) for command description.\nCommands:\n'help' or 'h'\n'dd' or 'dadata'\n'settings' or 's'\n'exit' or 'q' or 'e'")
        return
    match args[0]:
        case "help" | "h":
            print("This command provides list of commands if called without arguments or a description of every command if called with a name of the command instead.")
        case "dd" | "dadata":
            print("Makes a call to dadata API to get exeact coordinates of given address. Arguments: query. To use this function you need to set your API token using settings command. Example:dd Новосибирск, Ленина 12")
        case "settigs" | "s":
            print("""Changes user settings. Settings are:
                  1.api_token - an API token for dadata requests. You can get it at https://dadata.ru/profile.
                  2.language - changes the language of dadata response (either 'ru' or 'en'). Does not affect language of this programm.
                  3.max_count - defines how much results dadata api shows you. Can be in range from 1 to 20.""")
        case "exit" | "q" | "e":
            print("Finishes work of a programm. This is the prefferable way to stop a programm.")
        case _:
            print("Unknown help agruments. For general help type 'help' with no arguments.")