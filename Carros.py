class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def apresentar_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


meu_carro = Carro(marca="Volkswagen", modelo="GOL", ano=2012)

meu_carro.apresentar_carro()
