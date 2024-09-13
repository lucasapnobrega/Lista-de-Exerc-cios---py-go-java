class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def exibir_detalhes(self):
    print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Renault", "Sandero", 2018)
carro2 = Carro("volkswagen ", "Gol", 2015)
carro3 = Carro("Jeep", "Compass", 2023)

carro1.exibir_detalhes()
carro2.exibir_detalhes()
carro3.exibir_detalhes()