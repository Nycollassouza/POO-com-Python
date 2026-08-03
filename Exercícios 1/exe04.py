class Cliente:
    clientes = []
    def __init__(self, nome, idade, genero):
        self.nome = nome 
        self.idade = idade
        self.genero = genero 
        Cliente.clientes.append(self)

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} | {cliente.genero}')

cliente1 = Cliente('Nycollas', 19, 'Homem')
cliente2 = Cliente('Daniela', 45, 'Mulher')
cliente3 = Cliente('Heloísa', 20, 'Mulher')

Cliente.listar_clientes()