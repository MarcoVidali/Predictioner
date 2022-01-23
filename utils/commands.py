def help(commands:list):
    import tabulate
    return tabulate.tabulate(commands, tablefmt = "fancy_grid") + "\n"

def list_projects(projects:list):
    result = ""
    for project in projects: result += f"{project}\n"
    return result

def create(data_path:str, name:str) -> None:
    file:object = open(data_path + name, "a")
    file.close()

def remove(data_path:str, name:str) -> None:
    import os
    os.remove(data_path + name)

def load(projects:list, name:str, section:str) -> str:
    if name in projects: return name
    return section

def list_data(data_path:str, name:str) -> str:
    with open(data_path + name, "r") as file:
        data = file.read()
    return data

def add(data_path:str, name:str, value:int) -> None:
    file = open(data_path + name, "a")
    file.write(f"{float(value)}\n")
    file.close()

def add_file(data_path:str, name:str, file_path:str) -> None:
    file_to_add = open(file_path).read()
    for x in file_to_add.split(","): add(data_path, name, x)