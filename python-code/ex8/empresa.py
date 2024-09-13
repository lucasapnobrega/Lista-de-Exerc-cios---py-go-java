from empregado import Empregado

class Empresa:
  def __init__(self, nome):
    self.nome = nome
    self.empregados = []

  def adicionar_empregado(self, empregado):
    self.empregados.append(empregado)

  def listar_empregados(self):
    for empregado in self.empregados:
      print(empregado)