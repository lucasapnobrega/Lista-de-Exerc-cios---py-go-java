from professor import Professor

class Escola:
  def __init__(self, nome):
    self.nome = nome
    self.professores = []

  def adicionar_professor(self, professor):
    if professor not in self.professores:
      self.professores.append(professor)

  def __str__(self):
    return self.nome