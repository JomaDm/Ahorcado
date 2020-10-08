from palabra import *   
from ahorcado import *
from console import *

class Game():
  def __init__(self):
    self.palabra_actual = Palabra()
    self.dibujo_ahorcado = Ahorcado()
    self.dibujo_palabra = list()
    self.gameOver = False
    self.ganar = False

  def play(self):
    """
    Inicia el juego
    """
    
    self.palabra_actual.cargarPalabra()
    self.dibujo_palabra = ["_" for i in self.palabra_actual.obtenerPalabra()]
    clearScreen()
    self.dibujo_ahorcado.imprimir()
    
    while( not self.dibujo_ahorcado.obtenerFin() and not self.gameOver ):
      
      
      print("\tPalabra: "+" ".join(self.dibujo_palabra))
      intento = str(input("Intento (letra o palabra):"))
      
      puntuacion = self.compararAPalabraActual(intento)      
      
      if(puntuacion == 0):
        self.dibujo_ahorcado.next()
      clearScreen()
      self.dibujo_ahorcado.imprimir()
    
    print("Fin del juego\nPalabra:",self.palabra_actual.obtenerPalabra())
    if(self.ganar):
      print("Felicidades!!!!")
    else:
      print("Suerte para la proxima")
    input()
    clearScreen()
      
  
  
  def compararAPalabraActual(self, intento):
    """
    docstring
    """
    existe_letra = 0
    if(len(intento) == 1):
      for i,e in enumerate(self.palabra_actual.obtenerPalabra()):
        if(e == intento):
          self.dibujo_palabra[i] = e
          existe_letra+=1
      
      if("_" not in self.dibujo_palabra):
        self.gameOver = True
        self.ganar = True
              
    else:
      if (self.palabra_actual.obtenerPalabra() == intento):
        self.gameOver = True
        self.ganar = True
        existe_letra = len(self.palabra_actual.obtenerPalabra())
        
    return existe_letra
      
      
      
    
    
      