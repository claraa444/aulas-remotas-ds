class Veiculo: #classe mae
    def __init__(self, cor, modelo, ano, marca):
      self.cor = cor
      self.modelo = modelo
      self.ano = 0
      self.marca = marca

class Carro(Veiculo): #classe filha
    def __init__(self, cor, modelo, ano, marca, numero_portas):
      super().__init__(cor, modelo, ano, marca)
      self.numero_portas = 0 
