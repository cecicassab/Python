def mdc(numeros):
    def calc(divisor):
        #se a soma dos restos da divisão de cada elemento da lista pelo divisor testado for 0
        #significa que o divisor divide todos os numeros da lista
        #portanto é o mdc, logo retorna divisor
        #caso não seja, retorna a fução calc para testar o número logo abaixo
        return divisor if sum(map(lambda x: x%divisor, numeros)) == 0 else calc(divisor-1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21,7])) #7
    print(mdc([125,40])) #5
    print(mdc([9,564,66,3])) #3
    print(mdc([55,22])) #11
    print(mdc([15,150])) #15
    print(mdc([7,9])) #1