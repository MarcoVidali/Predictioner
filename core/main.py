def main() -> None:
    import json

    from utils import console, commands, files, prediction
    from containers import consts

    # variables
    section:str = "~"
    run:bool = True

    # loading containers
    with open("./containers/paths.json", "r") as file:
        DATA_PATH= json.load(file)["data"]

    while run:
        try:
            console.clear()

            # loading projects
            projects_list:list = files.get_proejects(DATA_PATH)

            # getting command
            command:str = input(f"{section}> ")
            action:str = command.split(" ")[0]
            try: argument:str = command.split(" ")[1]
            except: pass

            # processing command
            if section == "~":
                if action == "help": input(commands.help(consts.COMMANDS))
                elif action == "back": run = False
                elif action == "list": input(commands.list_projects(projects_list))
                elif action == "create": commands.create(DATA_PATH, argument)
                elif action == "remove": commands.remove(DATA_PATH, argument)
                elif action == "load":
                    section = commands.load(projects_list, argument, section)

            elif section in projects_list:
                if action == "help": input(commands.help(consts.COMMANDS))
                elif action == "back": section = "~"
                elif action == "add":
                    if argument[0] == '"' and argument[len(argument) - 1] == '"':
                        argument = argument.replace('"', "")
                        commands.add_file(DATA_PATH, section, argument)
                    else: commands.add(DATA_PATH, section, argument)
                elif action == "list": input(commands.list_data(DATA_PATH, section))
                elif action == "predict":
                    sequence:list = commands.list_data(DATA_PATH, section).split("\n")
                    sequence.pop()

                    input(f"Prediction/s: {prediction.predict(sequence, int(argument))}\n")

        except: pass