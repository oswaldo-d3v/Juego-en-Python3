import os


def convertir_path(path):
    return os.path.join(path)


def existe_fichero(path):
    return os.path.exists(path)
