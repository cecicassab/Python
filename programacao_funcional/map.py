lista_1 = [1,2,3]
dobro = map(lambda x: x*2, lista_1)
print(list(dobro))


lista_2 = [
    {'Nome': 'Maria', 'Idade': 4},
    {'Nome': 'José', 'Idade': 3},
    {'Nome': 'Antonio', 'Idade': 5}
]

nomes = map(lambda pessoa: pessoa['Nome'], lista_2)
print(list(nomes))

idades = map(lambda pessoa: pessoa['Idade'], lista_2)
print(list(idades))

string = map(lambda pessoa: f'{pessoa["Nome"]} tem {pessoa["Idade"]}', lista_2)
print(list(string))