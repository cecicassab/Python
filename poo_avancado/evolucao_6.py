from abc import ABCMeta, abstractproperty


class Humano(metaclass = ABCMeta):
    #atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self,nome):
        self.nome = nome
        self._idade = None
    
    @property    
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,idade):
        if idade < 0:
            raise ValueError("Idade não pode ser um valor negativo")
        self._idade = idade
        
    @abstractproperty
    def inteligente(self):
        pass
        
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
    
    @property
    def inteligente(self):
        return False
    
    
class Sapiens(Humano):
    especie = Humano.especies()[-1]
    
    @property
    def inteligente(self):
        return True
    
        
anonimo = Humano('anonimo')
jose = Sapiens('Jose')
gronk = Neanderthal('Gronk')

try:
    anonimo.inteligente()
except NotImplementedError:
    print('classe abstrata')
    
print(f'{jose.nome} da classe {jose.__class__.__name__} é inteligente. {jose.inteligente}')
