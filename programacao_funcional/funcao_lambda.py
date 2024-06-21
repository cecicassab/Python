compras = (
    {'quantidade': 2, 'preço': 23,},
    {'quantidade': 5, 'preço': 55,},
    {'quantidade': 9, 'preço':40}
)

totais = tuple(
    map(
        lambda compra:  compra['quantidade'] * compra['preço'],
        compras
    )
)


print(f'Preços totais: {totais}')
print(f'Total geral: {sum(totais)}')
