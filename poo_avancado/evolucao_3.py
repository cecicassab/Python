class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self,nome):
        self.nome = nome
        self._idade = None
        
    def get_idade(self):
        return self._idade
    
    def set_idade(self,idade):
        if idade < 0:
            raise ValueError("Idade não pode ser um valor negativo")
        self._idade = idade
        
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
    
        
jose = Sapiens("Jose")
jose.set_idade(40)
print(f'Nome: {jose.nome} Idade: {jose.get_idade()}')
