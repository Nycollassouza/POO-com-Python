class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Profissão: {self._profissao}'

    def aniversario(self):
        self._idade += 1
    
    @property
    def saudacao(self):
        if self._profissao: 
            return f'Olá, sou {self._nome}, trabalho como {self._profissao}'
        else:
            return f'Olá, sou {self._nome}'


pessoa1 = Pessoa('Nycollas', 19, 'Programador')
print(pessoa1)
print(pessoa1.saudacao)
