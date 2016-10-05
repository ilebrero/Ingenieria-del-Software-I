class Caracteristica:
  _memo = dict()

  def __new__(cls, nombre):
    return cls._memo.setdefault(nombre, super().__new__(cls))

  def __init__(self, nombre):
    self.nombre = nombre

  def __str__(self):
    return self.nombre
