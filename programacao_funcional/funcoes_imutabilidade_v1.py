from functools import reduce
from operator import add


valores = [0, 45, 32, 90, 123]

#nao altera a lista
print(sorted(valores))
print(list(reversed(valores)))
print(valores)

#altera a lista
#valores.sort()
#valores.reversed()

#exemplos de funções que não alteram valores
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
