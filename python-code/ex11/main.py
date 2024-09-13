from funcionario_horista import FuncionarioHorista
from funcionario_assalariado import FuncionarioAssalariado

def main():
  horista = FuncionarioHorista("Lucas", 180, 25)
  assalariado = FuncionarioAssalariado("Eduarda", 3000)

  print(f"Salário do {horista.nome}: {horista.calcular_salario()}")
  print(f"Salário da {assalariado.nome}: {assalariado.calcular_salario()}")

if __name__ == "__main__":
  main()