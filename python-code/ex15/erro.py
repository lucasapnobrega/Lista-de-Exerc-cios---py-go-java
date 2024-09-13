class SaldoInsuficienteException(Exception):
  def __init__(self, mensagem="Saldo insuficiente para a operação"):
    self.mensagem = mensagem
    super().__init__(self.mensagem)

class ContaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo

  def depositar(self, valor):
    self.__saldo += valor

  def sacar(self, valor):
    if valor > self.__saldo:
      raise SaldoInsuficienteException()
    self.__saldo -= valor

  def obter_saldo(self):
    return self.__saldo

def main():
  conta = ContaBancaria(200)
  
  try:
    conta.sacar(300)
  except SaldoInsuficienteException as e:
    print(e)

if __name__ == "__main__":
  main()