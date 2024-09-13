class Configuracao:
  _instancia = None

  def __new__(cls, *args, **kwargs):
    if cls._instancia is None:
      cls._instancia = super(Configuracao, cls).__new__(cls, *args, **kwargs)

      cls._instancia.configuracoes = {}
    return cls._instancia

  def __init__(self):
    if not hasattr(self, 'inicializado'):
      self.inicializado = True
      self.configuracoes = {}

  def set_configuracao(self, chave, valor):
    self.configuracoes[chave] = valor

  def get_configuracao(self, chave):
    return self.configuracoes.get(chave, None)

def main():
  config1 = Configuracao()
  config2 = Configuracao()

  config1.set_configuracao("url", "http://exemplourl.com")
  print(config2.get_configuracao("url"))

  print(config1 is config2)  

if __name__ == "__main__":
  main()