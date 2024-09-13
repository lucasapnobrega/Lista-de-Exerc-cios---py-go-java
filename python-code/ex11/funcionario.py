from abc import ABC, abstractmethod

class Funcionario(ABC):
  def __init__(self, nome):
    self.nome = nome

  @abstractmethod
  def calcular_salario(self):
    pass