from random import randint

chave = randint(0,100)
numero_usuario = -1

while numero_usuario != chave:
    numero_usuario = int(input('Digite um número de 0 a 100: '))
    
print(f'nùmero encontrado! Resposta correta: {chave}')