from math import pi
import sys

def circulo(raio):
    print('Area do circulo:' , pi * float(raio)**2)


if __name__ == '__main__':
    raio = sys.argv[1]
    circulo(raio)
