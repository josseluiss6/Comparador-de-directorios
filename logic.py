import os
from pathlib import Path
import shutil

# /home/solve/Documentos/Python/GUI/Lol
def listContent(directory):
    # Devuelve una tupla de sets con los archivos y las carpetas
    docs = set(e for e in os.listdir(directory) if os.path.isfile(os.path.join(directory, e)))
    folders = set(e for e in os.listdir(directory) if os.path.isdir(os.path.join(directory, e)))
    return (docs, folders)

