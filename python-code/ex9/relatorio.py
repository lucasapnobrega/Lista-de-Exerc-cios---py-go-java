from imprimivel import Imprimivel

class Relatorio(Imprimivel):
  def __init__(self, conteudo):
    self.conteudo = conteudo
  
  def imprimir(self):
    print(f"Relatório: {self.conteudo}")