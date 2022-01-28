def main() -> None:
    import json

    from utils import console, commands, files, prediction
    from containers import consts

    # variables
    section:str = "~"
    run:bool = True

    # loading containers
    with open("./containers/paths.json", "r") as file:
        DATA_PATH:str = json.load(file)["data"]

    while run:
        try:
            console.clear()

            # loading projects
            projects_list:list = files.get_proejects(DATA_PATH)

            # getting command
            if section != "~": command:str = input(f"project({section}) > ")
            else: command:str = input(f"{section}> ")
            action:str = command.split(" ")[0]
            try: argument:str = command.split(" ")[1]
            except: pass

            # processing command
            if section == "~":
                if action == "help": input(f"\n{commands.help(consts.COMMANDS)}\n")
                elif action == "back": run = False
                elif action == "list": input(f"\n{commands.list_projects(projects_list)}\n")
                elif action == "create": commands.create(DATA_PATH, argument)
                elif action == "remove": commands.remove(DATA_PATH, argument)
                elif action == "load":
                    section = commands.load(projects_list, argument, section)
                elif action == "": pass
                else:
                    # feedback
                    input(f"\nCommand \"{action}\" does not exist...\n\n")

            elif section in projects_list:
                if action == "help": input(f"\n{commands.help(consts.COMMANDS)}\n")
                elif action == "back": section = "~"
                elif action == "add":
                    if argument[0] == '"' and argument[len(argument) - 1] == '"':
                        argument = argument.replace('"', "")
                        commands.add_file(DATA_PATH, section, argument)
                    else: commands.add(DATA_PATH, section, argument, True)
                elif action == "list": input(f"\n{commands.list_data(DATA_PATH, section)}\n")
                elif action == "reset": commands.reset(DATA_PATH, section)
                elif action == "predict":
                    # showing sequence
                    sequence:list = commands.list_data(DATA_PATH, section).split("\n")
                    sequence.pop()
                    sequence_function, result = prediction.predict(sequence, int(argument))

                    # showing plot
                    if sequence_function != "Unknown function...":
                        input(f"\nSequence function: {sequence_function}\nPrediction/s: {result}\n")
                        prediction.plot_function(sequence_function)
                    else:
                        input(f"\nSequence function: {sequence_function}\nPrediction/s: {result}\n\n")

                elif action == "": pass
                else:
                    # feedback
                    input(f"\nCommand \"{action}\" does not exist...\n\n")
        except:
            # feedback
            input("\nAn error occurred...\n\n")