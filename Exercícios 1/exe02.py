class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, avaliacao):
        self.nome = nome 
        self.categoria = categoria 
        self.ativo = False
        self.avaliacao = avaliacao
        Restaurante.restaurantes.append(self)

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.avaliacao}')

restaurante1 = Restaurante('Japa', 'Botiquim', 10)

Restaurante.listar_restaurantes()