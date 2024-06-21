from math import pi

def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    raio = input('Digite o valor do raio: ')
    area = circulo(raio)
    
print('Área do circulo: ', area)
