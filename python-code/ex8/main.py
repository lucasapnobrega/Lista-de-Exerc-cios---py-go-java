from empresa import Empresa
from empregado import Empregado

def main():
  empresa = Empresa("TechCorp")

  empregado1 = Empregado("Alice", "Desenvolvedora", 70000)
  empregado2 = Empregado("Bob", "Analista", 60000)
  
  empresa.adicionar_empregado(empregado1)
  empresa.adicionar_empregado(empregado2)

  print(f"Empregados da {empresa.nome}:")
  empresa.listar_empregados()

if __name__ == "__main__":
  main()