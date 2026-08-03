class ContaBancaria: 
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False 

    def __str__(self):
        return f'Titular da Conta: {self._titular} \nSaldo: R${self._saldo}\nEstado da Conta: {self._ativo}'

    def ativar_conta(self):
        self._ativo = not self._ativo

conta1 = ContaBancaria('Nycollas', 1900)
conta1.ativar_conta()
print(conta1._titular)