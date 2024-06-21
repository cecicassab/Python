from random import randint

def dado():
    return randint(1,6)


for i in range(1,7):
    if i%2 !=0:
        continue
    if i == dado():
        print("ACERTOU", i)
        break
else:
    print("Não acertou")