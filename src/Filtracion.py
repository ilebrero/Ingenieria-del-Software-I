from Direccion import *
from CalculadorDeDistancias import *

class Filtracion:

  def __init__(self, bares):
    self.bares = bares

  def listar(self):
    for bar in self.bares.listar():
      try:
        if self.cumple_condicion(bar):
          yield bar
      except:
        pass

class FiltracionCalificacion(Filtracion):

  def __init__(self, bares, registro, atributo, puntaje):
    super().__init__(bares)
    self.atributo = atributo
    self.puntaje = puntaje
    self.registro = registro

  def cumple_condicion(self, bar):
      return self.puntaje <= self.registro.obtener_promedio(bar, self.atributo)

class FiltracionDireccion(Filtracion):

  def __init__(self, bares, registro, direccion, radio):
    super().__init__(bares)
    self.registro = registro
    self.direccion = Direccion(direccion)
    self.calculador_de_distancias = CalculadorDeDistancias()
    self.radio = radio

  def cumple_condicion(self, bar):
      distancia = self.calculador_de_distancias.distancia_entre(bar.direccion, self.direccion)
      return distancia <= self.radio
