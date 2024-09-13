class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def __add__(self, other):
    if isinstance(other, Produto):
      return Produto(self.nome + " & " + other.nome, self.preco + other.preco)
    return NotImplemented

  def __str__(self):
    return f"{self.nome} - R${self.preco:.2f}"

def main():
  produto1 = Produto("Produto A", 100.00)
  produto2 = Produto("Produto B", 50.00)
  
  produto3 = produto1 + produto2

  print(produto1)  
  print(produto2)
  print(produto3)

if __name__ == "__main__":
  main()