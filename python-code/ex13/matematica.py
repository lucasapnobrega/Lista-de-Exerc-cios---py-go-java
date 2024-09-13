class Matematica:
  @staticmethod
  def fatorial(n):
    if n == 0:
      return 1
    else:
      return n * Matematica.fatorial(n - 1)

def main():
  num = 6
  resultado = Matematica.fatorial(num)
  print(f"O fatorial de {num} é {resultado}")

if __name__ == "__main__":
  main()