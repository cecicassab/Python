class Pessoa:
    def __init__(self,nome,idade):
        self.idade = idade
        self.nome = nome
        
    def __str__(self):
        return f'Nome: {self.nome} / Idade: {self.idade}'
    
    def isAdult(self):
        return True if self.idade >= 18 else False