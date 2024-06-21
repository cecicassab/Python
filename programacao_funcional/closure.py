def multiplicar(x):
    def calcula(y):
        return x * y
    return calcula


dobro = multiplicar(2)
triplo = multiplicar(3)

print(f'O triplo de 3 é {triplo(3)}')
print(f'O dobro de 7 é {dobro(7)}')
