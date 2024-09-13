from relatorio import Relatorio
from contrato import Contrato

def main():
  relatorio = Relatorio("Relatório Anual")
  contrato = Contrato("Contrato de Trabalho")

  relatorio.imprimir()
  contrato.imprimir()

if __name__ == "__main__":
  main()