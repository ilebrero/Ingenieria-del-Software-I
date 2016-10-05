from Ubicacion import *


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

class FiltracionUbicacion(Filtracion):

  def __init__(self, bares, registro, ubicacion, radio):
    self.bares = bares
    self.registro = registro
    self.ubicacion = Ubicacion(ubicacion)
    self.calculador_de_distancias = CalculadorDeDistancias()
    self.radio = radio

  def listar(self):
    for bar in self.bares.listar():
      distancia = self.calculador_de_distancias.distancia_entre(bar.ubicacion, self.ubicacion)
      if distancia <= self.radio:
        yield bar

