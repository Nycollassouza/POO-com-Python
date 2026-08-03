class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano 
        Carro.carros.append(self)

    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')


carro1 = Carro('Fox', 'Vermelho', 2006)
carro2 = Carro('Face', 'Prata', 2010)

Carro.listar_carros()