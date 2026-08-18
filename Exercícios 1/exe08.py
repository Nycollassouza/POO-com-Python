class Livro: 
    def __init__(self, titulo, autor, ano_de_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_de_publicacao = ano_de_publicacao
        self._disponivel = True
    
    def __str__(self):
        mensagem = f"Titulo: {self._titulo}\nAutor: {self._autor}\nAno de Publicação: {self._ano_de_publicacao}\nStatus: {"Diponível" if self._disponivel else "Não disponivel"}"
        return mensagem

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livro if Livro.ano_de_publicacao == ano and livro._disponivel]
        return livros_disponiveis



# livro1 = Livro("O Principe", "Nicolau Maquiavel", 1750)
# livro1.emprestar()
# livro2 = Livro("Entre o Bem e o Mal", "Nietzshe", 1800)
# print(livro1)
# print('*' * 25)
# print(livro2)

