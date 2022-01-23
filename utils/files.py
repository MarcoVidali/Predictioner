def get_proejects(data_path:str) -> list:
    import os
    return [f for f in os.listdir(data_path)
           if os.path.isfile(os.path.join(data_path, f))]