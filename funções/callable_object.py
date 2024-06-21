from typing import Any


class Potencia:
    
    def __init__(self, expoente):
        self.expoente = expoente
        
        
    def __call__(self, base):
        return base ** self.expoente
    

quadrado = Potencia(2)
cubo = Potencia(3)

print(f'3² = {quadrado(3)}')
print(f'3³ = {cubo(3)}')
print(f'9³ = {Potencia(3)(9)}')