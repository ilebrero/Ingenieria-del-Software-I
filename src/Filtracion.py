class Filtracion:
  pass

class FiltracionCalificacion(Filtracion):
  def __init__(self, bares, registro, atributo, puntaje):
    self.atributo = atributo
    self.puntaje = puntaje
    self.registro = registro
    self.bares = bares

  def listar(self):
    for bar in self.bares.listar():
      try:
        if self.puntaje <= self.registro.obtener_promedio(bar, self.atributo):
          yield bar
      except:
        pass
