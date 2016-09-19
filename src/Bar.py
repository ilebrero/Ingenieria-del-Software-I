from Ubicacion import *

class Bar:

  def __init__(self, nombre, direccion, atributos):
    self.nombre = nombre 
    self.ubicacion = Ubicacion(direccion)
    self.atributos = atributos

  # FALTA METODO NOMBRE DE BAR

  def str_con_calificacion(self, registro):
    res  =       "┌─────────────────────────────────────────────────────────┐\n"
    res +=       "│ " + self.nombre.ljust(55)                           + " │\n"
    res +=       "│ " + str(self.ubicacion).ljust(55)                   + " │\n"
    if self.atributos:
        res +=   "├─────────────────────────────────────────────────────────┤\n"
        for atributo in self.atributos:
          try:
            p = registro.obtener_promedio(self, atributo)
            atr = str(atributo) + " (★ " + "{:.1f}".format(p) + ")"
          except:
            atr = str(atributo)
          res += "│ " + atr.ljust(55)                                   + " │\n"
    res +=       "└─────────────────────────────────────────────────────────┘"
    return res

  def __str__(self):
    return self.str_con_calificacion(None)
