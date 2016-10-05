class RegistroDeCalificaciones():

  def __init__(self):
    self.registro = [] # lista de Calificacion

  def agregar(self, calificacion):
    self.registro.append(calificacion)

  def obtener_promedio(self, bar, caracteristica):
    res = [calif.puntaje for calif in self.registro if calif.bar == bar and calif.caracteristica == caracteristica]
    try:
      return sum(res)/len(res)
    except ZeroDivisionError:
      raise Exception("Bar no tiene calificaciones de " + str(caracteristica))
