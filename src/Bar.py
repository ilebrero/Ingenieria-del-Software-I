from Ubicacion import *

class Bar:

  def __init__(self, nombre, direccion, atributos):
    self.nombre = nombre 
    self.ubicacion = Ubicacion(direccion)
    self.atributos = atributos

  # FALTA METODO NOMBRE DE BAR

  def __str__(self):
    res = "Nombre: " + self.nombre + "\nDireccion: " + str(self.ubicacion) + "\nAtributos: "
    for atributo in self.atributos:
      res += str(atributo)
    
    return res
