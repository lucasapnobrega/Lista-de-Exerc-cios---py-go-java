from funcionario import Funcionario

class FuncionarioHorista(Funcionario):
  def __init__(self, nome, horas_trabalhadas, valor_hora):
    super().__init__(nome)
    self.horas_trabalhadas = horas_trabalhadas
    self.valor_hora = valor_hora

  def calcular_salario(self):
    return self.horas_trabalhadas * self.valor_hora