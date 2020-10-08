from game import *

if __name__ == "__main__":
    jugar = True
    
    while(jugar):
      
      opcion = int(input("Ahorcado !!!!\n\n1.Jugar\n2.Agregar palabras al diccionario\n3.Como jugar\n4.Salir\nOpcion:"))
      
      if(opcion == 1):
        game = Game()        
        game.play()
        del game
      elif(opcion == 2):
        nueva_palabra = input("Escribe la nueva palabra:")
        Palabra.guardarPalabra(nueva_palabra)
        clearScreen()
      elif(opcion == 3):
        print("Deberas escribir una letra o una palabra\ny se vera reflejado en el tablero\nsi la letra se encuentra dentro de la palabra,")
        print("las letras en cada posicion se veran, sino\nel ahorcado se ira construyendo\n\nImportante: las palabras usadas no llevan acento")
      elif(opcion == 4):
        jugar = False