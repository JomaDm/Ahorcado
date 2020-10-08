import os
from sys import platform
def clearScreen():
    """Description: Funcion que detecta el sistema operativo y relaciona su comando para borrar la pantalla
    """
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")