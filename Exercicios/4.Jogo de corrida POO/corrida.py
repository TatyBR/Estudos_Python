from random import randint

class Carro:

    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.distancia = 0
    
    def percorrer_distancia(self, distancia):
        self.distancia += distancia
    
def iniciar_jogo():
    print('*************************************************************************')
    print('Este é um jogo de corrida! Defina os carros:')
    print('*************************************************************************')
    marca1 = input('Carro_1: ')
    cor1 = input('Cor do Carro_1: ')
    ano1 = input('Ano Carro_1: ')
    marca2 = input('Carro_2: ')
    cor2 = input('Cor do Carro_2: ')
    ano2 = input('Ano Carro_2: ')
    carro1 = Carro(marca1,cor1,ano1)
    carro2 = Carro(marca2,cor2,ano2)

    while True:
        carro1.percorrer_distancia(randint(0, 10))
        carro2.percorrer_distancia(randint(0, 10))

        if carro1.distancia >= 100 and carro1.distancia > carro2.distancia:
            print(f'\nO carro vencedor foi: {carro1.marca} {carro1.cor} do ano de: {carro1.ano}!!')
            print(f'A distância percorrida pelo vencedor foi:{carro1.distancia}')
            print(f'A distância percorrida pelo perdedor foi: {carro2.distancia}')
            break

        if carro2.distancia >= 100 and carro2.distancia > carro1.distancia:
            print(f'\nO carro vencedor foi {carro2.marca} {carro2.cor} do ano de: {carro2.ano}!!')
            print(f'A distância percorrida pelo vencedor foi: {carro2.distancia}.')
            print(f'A distância percorrida pelo perdedor foi: {carro1.distancia}.')
            break

iniciar_jogo()