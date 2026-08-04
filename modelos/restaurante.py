from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria}'

    @classmethod # Esse é um método da classe
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property   
    def ativo(self): 
        return '✅' if self._ativo else '❌'

    def alternar_estado(self): # Esse é um método de instância e não um método de classe
        self._ativo = not self._ativo # caso o valor seja Falso passa a ser Verdadeiro e caso o valor seja Verdadeiro passa a ser Falso

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0 
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media =  round(soma_das_notas / len(self._avaliacao), 1)
        return media