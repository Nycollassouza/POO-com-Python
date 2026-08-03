class ClienteBanco: 
    clientes = []
    def __init__(self, nome, idade, saldo, tipo_da_conta):
        self._nome = nome.title()
        self._idade = idade
        self._saldo = saldo
        self._tipo_da_conta = tipo_da_conta
        self._ativo = False
        ClienteBanco.clientes.append(self)
    
    @classmethod
    def listar_clientes(cls):
        print(f'{'Nome'} | {'Idade'} | {'Saldo'} | {'Tipo da Conta'} | {'Status'}')
        for cliente in cls.clientes:
            print(f'{cliente._nome} | {cliente._idade} | {cliente._saldo} | {cliente._tipo_da_conta} | {cliente._ativo}')

cliente1 = ClienteBanco('Nycollas', 19, 1900, 'Corrente')
cliente2 = ClienteBanco('Heloísa', 20, 1000, 'Corrente')
cliente3 = ClienteBanco('Daniela', 45, 2900, 'Corrente')
ClienteBanco.listar_clientes()