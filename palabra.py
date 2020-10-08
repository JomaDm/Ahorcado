from random import randint
class Palabra():
  
  def __init__(self):
    """
    Crea un objeto palabra que será la palabra en cuestion del juego
    """
    self.palabra = str()    
  
  def establecerPalabra(self,palabra,file="diccionario.txt"):
    """
    Se establece una palabra para el juego
    """
    self.palabra = palabra
    
    with open(file,"a") as archivo_dicc:
      archivo_dicc.write("\n"+palabra)
  
  def cargarPalabra(self,file="diccionario.txt"):
    """
    file: archivo que se desea abrir
    ret: habilitar el retorno de la palabra
    Escoge una palabra al azar del diccionario especificado
    """    
    lista_palabras = list()
    with open(file,"r") as archivo_dicc:
      lista_palabras = archivo_dicc.readlines()
        
    self.palabra = lista_palabras[randint(0,len(lista_palabras)-1)]    
    print(self.palabra)
    