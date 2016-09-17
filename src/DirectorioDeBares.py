class DirectorioDeBares:

  def __init__(self):
    self.lista_de_bares = []

  def agregar(self, bar):
    self.lista_de_bares.append(bar)

  def listar(self):
    for bar in self.lista_de_bares:
      yield bar
