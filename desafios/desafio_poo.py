from loja import Cliente,Vendedor,Compra
from datetime import datetime

def main():
    
    a = Vendedor('Ana', 24 , 3200)
    b = Cliente('Bruna', 17)
    c = Cliente('Carla', 56)
    compra1 = Compra(a,datetime.now(),350)
    compra2 = Compra(a,datetime.now(),540)
    compra3 = Compra(a,datetime.now(),987)
    
    b.registra_compra(compra1)
    b.registra_compra(compra2)
    b.registra_compra(compra3)

    print(b.get_data_ultima_compra())
    print(b.total_compras())
    
    print(c)
    print(a)
    print(f'{b.nome} não é adulta') if not b.isAdult() else print(f'{b.nome} é adulta')
    
    for compra in b:
        print(f'Compra realizada pelo(a) vendedor(a) {compra.vendedor.nome} na data {compra.data} no valor de {compra.valor}')
    
    
if __name__ == '__main__':
    main()