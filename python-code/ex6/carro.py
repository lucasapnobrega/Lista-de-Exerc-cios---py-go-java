class Motor:
  def __init__(self, tipo):
    self.tipo = tipo

  def exibir_tipo(self):
    return f"Tipo de motor: {self.tipo}"

class Carro:
  def __init__(self, marca, modelo, motor):
    self.marca = marca
    self.modelo = modelo
    self.motor = motor

  def exibir_detalhes(self):
    return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.motor.exibir_tipo()}"

motor = Motor("V8")
carro = Carro("Volswagen", "Golf", motor)

print(carro.exibir_detalhes())