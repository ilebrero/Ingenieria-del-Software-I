class Ubicacion:

  def __init__(self, direccion):
    self.direccion = direccion 

  def coordenadas(self, direccion):
    raise Exception("no esta hecho esto")

  def __str__(self):
    return self.direccion
