from math import pi

def circulo(raio):
    print('Area do circulo:' , pi * float(raio)**2)


if __name__ == '__main__':
    raio = input('Digite o valor do raio: ')
    circulo(raio)
