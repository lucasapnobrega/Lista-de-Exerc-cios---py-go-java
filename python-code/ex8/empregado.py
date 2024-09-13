class Empregado:
  def __init__(self, nome, cargo, salario):
    self.nome = nome
    self.cargo = cargo
    self.salario = salario

  def __str__(self):
    return f"{self.nome}, {self.cargo}, {self.salario}"