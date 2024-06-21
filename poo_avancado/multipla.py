class Animal:
    @property
    def capacidades(self):
        return ('comer','dormir','beber')
    
    
class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar','estudar','falar')
    
    
class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia','andar pelas paredes')
    
    
class HomemAranha(Homem,Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos',)
    
    
if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')
    
    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')
    
    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')
    
    