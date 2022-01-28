def help(commands:list):
    import tabulate
    return tabulate.tabulate(commands, tablefmt = "fancy_grid") + "\n"

def list_projects(projects:list):
    if len(projects) == 0:
        # feedback
        return "There are no projects...\n"
    
    result = ""
    for project in projects: result += f"{project}\n"
    return result

def create(data_path:str, name:str) -> None:
    file:object = open(data_path + name, "a")
    file.close()

    # feedback
    input(f"\nProject \"{name}\" created successfully!\n\n")

def remove(data_path:str, name:str) -> None:
    import os
    os.remove(data_path + name)
    
    # feedback
    input(f"\nProject \"{name}\" removed successfully!\n\n")

def load(projects:list, name:str, section:str) -> str:
    if name in projects: return name
    # feedback
    input(f"\nProject \"{name}\" does not exist...\n\n")
    return section

def list_data(data_path:str, name:str) -> str:
    with open(data_path + name, "r") as file: data = file.read()
    
    # feedback
    if len(data) == 0: return "This sequence has no terms...\n"

    return data

def add(data_path:str, name:str, value:int, feedback:bool) -> None:
    file = open(data_path + name, "a")
    file.write(f"{float(value)}\n")
    file.close()
        
    # feedback
    if feedback: input(f"\nTerm \"{value}\" addedd successfully!\n\n")

def add_file(data_path:str, name:str, file_path:str) -> None:
    file_to_add = open(file_path).read()
    for term in file_to_add.split(","): add(data_path, name, term, False)
    
    # feedback
    input("\nFile addedd successfully!\n\n")
    
def reset(data_path:str, name:str):
    f = open(data_path + name, "w")
    f.write("")
    f.close()
    
    # feedback
    input("\nProject resetted successfully!\n\n")