class ContaBancaria:
  def __init__(self, titular, saldo_inicial=0):
    self.__titular = titular
    self.__saldo = saldo_inicial

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      print(f"Depositado: R$ {valor:.2f}. Saldo atual: R$ {self.__saldo:.2f}")
    else:
      print("Valor do depósito deve ser positivo.")

  def sacar(self, valor):
    if valor > 0:
      if valor <= self.__saldo:
        self.__saldo -= valor
        print(f"Sacado: R$ {valor:.2f}. Saldo atual: R$ {self.__saldo:.2f}")
      else:
        print("Saldo insuficiente.")
    else:
      print("Valor do saque deve ser positivo.")

  def exibir_saldo(self):
    print(f"Saldo atual: R$ {self.__saldo:.2f}")

conta = ContaBancaria("Lucas", 2000)
conta.depositar(400)
conta.sacar(600)
conta.exibir_saldo()