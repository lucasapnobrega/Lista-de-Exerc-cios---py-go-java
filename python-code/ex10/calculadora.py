class Calculadora:
  def somar(self, *args):
    return sum(args)

def main():
  calc = Calculadora()
  
  print("Soma de 2 e 3:", calc.somar(2, 3))
  print("Soma de 1, 2 e 3:", calc.somar(1, 2, 3))

if __name__ == "__main__":
  main()