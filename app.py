from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_japones.receber_avaliacao('Nycollas', 10)
restaurante_japones.receber_avaliacao('Tamiris', 10)
restaurante_japones.receber_avaliacao('Daniela', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()