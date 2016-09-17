class RegistroDeCalificaciones():

  def __init__(self):
    self.registro = [] # lista de Calificacion

  def agregar(self, calificacion):
    self.registro.append(calificacion)

  # [TODO] hacer que a martin le guste el nombre
  def obtener_promedio(self, bar, atributo):
    res = [c.puntaje for c in self.registro if c.bar == bar and c.atributo == atributo]
    try:
      return sum(res)/len(res)
    except ZeroDivisionError:
      raise Exception("Bar no tiene calificaciones de " + str(atributo))
