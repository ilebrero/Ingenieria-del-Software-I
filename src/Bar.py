from Direccion import *

class Bar:

  # [TODO] tal vez debería recibir una ubicación en vez de una dirección
  def __init__(self, nombre, direccion, caracteristicas):
    self.nombre = nombre 
    self.direccion = Direccion(direccion)
    self.caracteristicas = caracteristicas

  # FALTA METODO NOMBRE DE BAR

  def str_con_calificacion(self, registro):
    res  =       "┌─────────────────────────────────────────────────────────┐\n"
    res +=       "│ " + self.nombre.ljust(55)                           + " │\n"
    res +=       "│ " + str(self.direccion).ljust(55)                   + " │\n"
    if self.caracteristicas:
        res +=   "├─────────────────────────────────────────────────────────┤\n"
        for caracteristica in self.caracteristicas:
          try:
            p = registro.obtener_promedio(self, caracteristica)
            car = str(caracteristica) + " (★ " + "{:.1f}".format(p) + ")"
          except:
            car = str(caracteristica)
          res += "│ " + car.ljust(55)                                   + " │\n"
    res +=       "└─────────────────────────────────────────────────────────┘"
    return res

  def __str__(self):
    return self.str_con_calificacion(None)
