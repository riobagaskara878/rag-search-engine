import json 

def loader(file_path) -> dict:
    with open(file_path) as file:
        movies = json.load(file)
    return movies