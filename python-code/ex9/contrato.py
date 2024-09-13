from imprimivel import Imprimivel

class Contrato(Imprimivel):
  def __init__(self, detalhes):
    self.detalhes = detalhes
  
  def imprimir(self):
    print(f"Contrato: {self.detalhes}")