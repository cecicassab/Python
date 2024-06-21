def mdc(numeros):
    menor = min(numeros)
    div = True
    for i in range(menor,0,-1):
        for j in numeros:
            if j%i !=0:
                div = False
                break
            else:
                div = True
        if div: return i


if __name__ == '__main__':
    print(mdc([21,7])) #7
    print(mdc([125,40])) #5
    print(mdc([9,564,66,3])) #3
    print(mdc([55,22])) #11
    print(mdc([15,150])) #15
    print(mdc([7,9])) #1