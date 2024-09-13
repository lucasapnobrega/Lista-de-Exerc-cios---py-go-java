from funcionario import Funcionario

class FuncionarioAssalariado(Funcionario):
  def __init__(self, nome, salario_mensal):
    super().__init__(nome)
    self.salario_mensal = salario_mensal

  def calcular_salario(self):
    return self.salario_mensal