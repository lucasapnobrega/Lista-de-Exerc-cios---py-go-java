class Professor:
  def __init__(self, nome):
    self.nome = nome
    self.escolas = []

  def adicionar_escola(self, escola):
    if escola not in self.escolas:
      self.escolas.append(escola)
      escola.adicionar_professor(self)

  def __str__(self):
    return self.nome
