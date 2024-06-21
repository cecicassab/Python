pessoas = [
    {'Nome': 'Maria', 'Idade': 4},
    {'Nome': 'José', 'Idade': 3},
    {'Nome': 'Antonio', 'Idade': 5},
    {'Nome': 'Mariana', 'Idade': 48},
    {'Nome': 'Lucas', 'Idade': 40},
    {'Nome': 'Cecilia', 'Idade': 19}
]

menores = filter(lambda p: p['Idade'] < 18, pessoas)
print(list(menores))

nome_grande = filter(lambda p: len(p['Nome']) > 6, pessoas)
print(list(nome_grande)) 
