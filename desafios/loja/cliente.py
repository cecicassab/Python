from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
        
    def __iter__(self):
        return self.compras.__iter__()
        
    def registra_compra(self,compra):
        self.compras.append(compra)
        
    def get_data_ultima_compra(self):
        return self.compras[-1].data
        
    def total_compras(self):
        soma = 0
        for compra in self:
            soma += compra.valor
        return soma