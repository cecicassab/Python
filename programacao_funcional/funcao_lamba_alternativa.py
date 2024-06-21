compras = (
    {'quantidade': 2, 'preço': 23,},
    {'quantidade': 5, 'preço': 55,},
    {'quantidade': 9, 'preço':40}
)


def calcular_preco(compra):
    return compra['quantidade'] * compra['preço']


totais = tuple(map(calcular_preco,compras))


print(f'Preços totais: {totais}')
print(f'Total geral: {sum(totais)}')