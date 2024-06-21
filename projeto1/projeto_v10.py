from math import pi
import sys
import errno

ERRO = '\033[91m'
NORMAL = '\033[0m'

def circulo(raio):
    print('Area do circulo:' , pi * float(raio)**2)
    
    
def help():
    print("É necessário informar o raio na linha de comando")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
        
    if not sys.argv[1].isnumeric():
        print(ERRO + "O argumento deve ser uma valor numérico" + NORMAL)
        sys.exit(errno.EINVAL)
        
    raio = sys.argv[1]
    circulo(raio)
