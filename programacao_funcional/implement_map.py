def mapear(function, list):
    lista = []
    for i in list:
        x = function(i)
        lista.append(x)
    return lista


"""
implementação do professor
def mapear(function, list):
    for elemento in list:
        yield funtion(elemento)
"""

print(list(mapear(lambda x: x**2, [2,3,4])))