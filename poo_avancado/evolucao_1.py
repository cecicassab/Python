class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self,nome):
        self.nome = nome
        
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
        
        
jose = Humano('jose')
gronk = Humano('gronk').das_cavernas()

print(f'jose.especie {jose.especie}')
print(f'gronk.especie {gronk.especie}')
