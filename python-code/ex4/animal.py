class Animal:
  def som(self):
    raise NotImplementedError("O método 'som' deve ser implementado pelas subclasses.")

class Cachorro(Animal):
  def som(self):
    return "Au Au"

class Gato(Animal):
  def som(self):
    return "Miau"

def exibir_som(animal):
  print(animal.som())

cachorro = Cachorro()
gato = Gato()

exibir_som(cachorro) 
exibir_som(gato) 