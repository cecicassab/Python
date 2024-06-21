def calc_imposto_total(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto*calc_imposto(**params)


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fat_mult=1):
    return 0.11 * fat_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.77
    preco_final = calc_imposto_total(preco_bruto, imposto_x, importado=True)
    preco_final = calc_imposto_total(preco_final,imposto_y, 
                                     explosivo=True, fat_mult=1.2)
    print(f'Preço final R${preco_final}')
