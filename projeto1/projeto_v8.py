from math import pi
import sys

def circulo(raio):
    print('Area do circulo:' , pi * float(raio)**2)
    
    
def help():
    print("É necessário informar o raio na linha de comando")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        circulo(raio)
