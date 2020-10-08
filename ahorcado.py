class Ahorcado():
  
  def __init__(self):
    """
    Se crea el objeto ahorcado, que será el dibujo del juego
    """
    self.fin = False
    self.estado = 0
    self.progeso = ["\t---------",
                    "\t|       |",
                    "\t|       ",
                    "\t|       ",
                    "\t|       ",
                    "\t-        "]                   
  def next(self):
    """
    Automata para dibujar el cuerpo del dibujo
    """
    if(self.estado == 1):
      self.fin = False
      self.progeso[2] = "\t|       0"
    elif (self.estado == 2):
      self.progeso[3] = "\t|      /"
    elif (self.estado == 3):
      self.progeso[3] = "\t|      / \\"
    elif (self.estado == 4):
      self.progeso[4] = "\t|       |"
    elif (self.estado == 5):
      self.progeso[5] = "\t|      / "
    elif (self.estado == 6):
      self.progeso[5] = "\t|      / \\"
    elif (self.estado == 7):
      for i in range(len(self.progeso)):
        self.progeso[i] = ""
      self.progeso[3] = "\tFin del juego"
      self.estado = -1
      self.fin = True
    self.estado+=1
    
    def obtenerFin(self):
      """
      docstring
      """
      return self.fin
    
  def imprimir(self):
    """
     docstring
    """
    print( "Fin:"+str(self.fin)+" Estado:"+str(self.estado)+"\nProgreso:\n"+"\n".join(self.progeso)    )
    
    
dibujo = Ahorcado()
print("Empieza")
print("\n".join(dibujo.progeso))
for i in range(8):
  dibujo.next()
  #print("\n".join(dibujo.progeso))
  dibujo.imprimir()
print("Fin")