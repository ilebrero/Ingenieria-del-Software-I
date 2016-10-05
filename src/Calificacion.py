class Calificacion():

  def __init__(self, bar, caracteristica, puntaje):
    if not (0 <= puntaje <= 5):
      raise Exception("Puntaje no está entre 0 y 5")
    self.bar = bar
    self.caracteristica = caracteristica
    self.puntaje = puntaje
