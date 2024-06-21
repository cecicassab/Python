from functools import reduce
from operator import add


valores = (0, 45, 32, 90, 123)

#nao altera a tupla
print(sorted(valores))
print(tuple(reversed(valores)))
print(valores)

#gera erro de execução, pois um dado do tipo tupla é imutável
#valores.sort()
#valores.reversed()

#exemplos de funções que não alteram valores
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
