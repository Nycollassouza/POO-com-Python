class Restaurante:

    def __init__(self, nome, categoria, avaliacao):
        self.nome = nome 
        self.categoria = categoria 
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante1 = Restaurante('Japa', 'Botiquim', 10)
print(restaurante1)