class Animal:
  def som(self):
    raise NotImplementedError("O método 'som' deve ser implementado pelas subclasses.")

class Cachorro(Animal):
  def som(self):
    return "Au Au"

class Gato(Animal):
  def som(self):
    return "Miau"

def exibir_sons(animais):
  for animal in animais:
    print(animal.som())

animais = [Cachorro(), Gato()]

exibir_sons(animais)