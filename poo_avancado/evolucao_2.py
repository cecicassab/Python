class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self,nome):
        self.nome = nome
        
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
        
    @staticmethod
    def especies():
        adjetivos = ('Habilis','Erectus','Neanderthalensis','Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]
    
    
class Neanderthal(Humano):
    especie = Humano.especies()[-2]
    
    
class Sapiens(Humano):
    especie = Humano.especies()[-1]
    
        
jose = Sapiens('Jose')
gronk = Neanderthal('Gronk')

print(f'evolução a partir da classe {", ".join(Humano.especies())}')
print(f'evolução a partir da instância {", ".join(jose.especies())}')

print(f'José é evoluido? {jose.is_evoluido()}')
print(f'Homo Sapiens é evoluido? {Sapiens.is_evoluido()}')