class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.velocidade = 0 

  def acelerar(self, incremento):  
    self.velocidade += incremento
    print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")

  def frear(self, decremento):
    self.velocidade -= decremento

    if self.velocidade < 0:
      self.velocidade = 0
      
    print(f"O carro freou. Velocidade atual: {self.velocidade} km/h")

  def exibir_velocidade(self):
    print(f"Velocidade atual: {self.velocidade} km/h")


carro = Carro("BMW", "M4", 2022)

carro.acelerar(60)   
carro.acelerar(150)
carro.frear(20)  
carro.exibir_velocidade() 
carro.frear(30)
carro.acelerar(50)
carro.exibir_velocidade()