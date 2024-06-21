from math import pi
import sys

def circulo(raio):
    print('Area do circulo:' , pi * float(raio)**2)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário passar o raio do círculo")
    else:
        raio = sys.argv[1]
        circulo(raio)
