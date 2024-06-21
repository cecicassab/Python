def dobro(x):
    return x*2


def quadrado(x):
    return x**2


if __name__ == '__main__':
    func = [dobro,quadrado] * 5
    for func,numero in zip(func, range(1,11)):
        print(f'executando função {func.__name__} para o valor {numero}: {func(numero)}')

    