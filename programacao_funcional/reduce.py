from functools import reduce


pessoas = [
    {'Nome': 'Maria', 'Idade': 4},
    {'Nome': 'José', 'Idade': 3},
    {'Nome': 'Antonio', 'Idade': 5},
    {'Nome': 'Mariana', 'Idade': 48},
    {'Nome': 'Lucas', 'Idade': 40},
    {'Nome': 'Cecilia', 'Idade': 19}
]

soma_idades = reduce(lambda idade,p: idade + p['Idade'], pessoas, 0)
print(soma_idades)

idades = map(lambda pessoa: pessoa['Idade'], pessoas)
menores = filter(lambda idade: idade < 18, idades)

soma_idades_menores = reduce(lambda idade, men: idade + men, menores, 0)
print(soma_idades_menores)