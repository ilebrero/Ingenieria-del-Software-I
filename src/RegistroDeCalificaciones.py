class RegistroDeCalificaciones():

  def __init__(self):
    self.registro = [] # lista de Calificacion

  def agregar(self, calificacion):
    self.registro.append(calificacion)

  # [TODO] hacer que a martin le guste el nombre
  def obtener_promedio(self, bar, atributo):
    res = [calif.puntaje for calif in self.registro if calif.bar == bar and calif.atributo == atributo]
    try:
      return sum(res)/len(res)
    except ZeroDivisionError:
      raise Exception("Bar no tiene calificaciones de " + str(atributo))
