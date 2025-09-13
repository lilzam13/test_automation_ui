import os

def create_folder():
    base =  "C:\\Users\\lilia\\Desktop"
    path = os.path.join(base, "python-robot", "DEMO_FOLDER")
    os.makedirs(path, exist_ok=True)

def create_subfolder(subfolder_name):
    base =  "C:\\Users\\lilia\\Desktop\\python-robot"
    path = os.path.join(base, "DEMO_FOLDER", subfolder_name)
    os.makedirs(path, exist_ok=True)

def concatenate_name(name, lastname1, lastname2):
    namec = f"Bienvenido al curso de Robot Framework: {name} {lastname1} {lastname2} "
    return namec

def validate_name(name):
    if name == "Liliana":
        return "Bienvenida Liliana"
    else:
        return "No se quien eres"
