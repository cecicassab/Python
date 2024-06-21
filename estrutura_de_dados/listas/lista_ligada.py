class No:
    def __init__(self,conteudo):
        self.conteudo = conteudo
        self.proximo = None
        
        
class ListaLigada:
    def __init__(self):
        self._inicio = None
        self._quantidade = 0
        
    @property
    def inicio(self):
        return self._inicio
    
    @property
    def quantidade(self):
        return self._quantidade
    
    def inserir_no_inicio(self,conteudo):
        no = No(conteudo)
        no.proximo = self._inicio
        self._inicio = no
        self._quantidade += 1
        
    def imprimir(self):
        atual = self._inicio
        for i in range(self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo
            
    def inserir(self,posicao,conteudo):
        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return
        no = No(conteudo)
        esq = self._celula(posicao-1)
        no.proximo = esq.proximo
        esq.proximo = no
        self._quantidade += 1
            
    def _celula(self,posicao):
        self._validar_posicao(posicao)
        atual = self.inicio
        for i in range(posicao):
            atual = atual.proximo
        return atual
        
    def _validar_posicao(self,posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida")
    
    def remover_do_inicio(self):
        removido = self.inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo
    
    def remover(self,posicao):
        if posicao == 0:
            self.remover_do_inicio()
        removido = self._celula(posicao)
        esq = self._celula(posicao-1)
        esq.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo
    
    def item(self,posicao):
        self._validar_posicao(posicao)
        no = self._celula(posicao)
        return no.conteudo
    
##a biblioteca padrão de python possui a função "list" que atua como lista encadeada