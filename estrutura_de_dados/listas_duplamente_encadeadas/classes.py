class No:
    def __init__(self,conteudo):
        self.conteudo = conteudo
        self.anterior = None
        self.proximo = None


class ListaDupla: 
    def __init__(self):
        self._inicio = None
        self._final = None
        self._quantidade = 0
        
    @property
    def inicio(self):
        return self._inicio
    
    @property
    def final(self):
        return self._final
    
    @property
    def quantidade(self):
        return self._quantidade
    
    def _inserir_em_lista_vazia(self,conteudo):
        no = No(conteudo)
        self._inicio = no
        self._final = no
        self._quantidade += 1
        
    def item(self,posicao):
        self._validar_posicao(posicao)
        no = self._celula(posicao)
        return no.conteudo
        
        
    def _validar_posicao(self,posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida")
    
    def _celula(self,posicao):
        self._validar_posicao(posicao)
        metade = self.quantidade//2
        if posicao < metade:
            atual = self.inicio
            for i in range(posicao):
                atual = atual.proximo
            return atual
        atual = self._final
        for i in range(posicao+1,self.quantidade)[::-1]:
            atual = atual.anterior
        return atual
        
    def inserir_no_inicio(self,conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        no = No(conteudo)
        no.proximo = self.inicio
        self._inicio = no
        self._inicio.anterior = no
        self._quantidade += 1
        
    def imprimir(self):
        atual = self.inicio
        for i in range(self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo
            
    def inserir_no_final(self,conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        no = No(conteudo)
        no.anterior = self.final
        no.proximo = None
        self.final.proximo = no
        self._final = no
        self._quantidade += 1
        
    def inserir(self,posicao,conteudo):
        if posicao == 0:
            return self.inserir_no_inicio(conteudo)
        if posicao == self.quantidade:
            return self.inserir_no_final(conteudo)
        esq =  self._celula(posicao-1)
        dir = esq.proximo
        no = No(conteudo)
        no.proximo = dir
        no.anterior = esq
        esq.proximo = no
        dir.anterior = no
        self._quantidade += 1
        
    def _remover_unico(self):
        if self.quantidade == 1:
            removido = self.inicio
            self._inicio = None
            self._final = None
            self._quantidade -= 1
            return removido.conteudo
        
    def remover_do_inicio(self):
        if self.quantidade == 1:
            return self._remover_unico()
        removido = self.inicio
        self._inicio = removido.proximo
        self._inicio.anterior = None
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo
    
    def remover_do_final(self):
        if self.quantidade == 1:
            return self._remover_unico()
        removido = self.final
        self._final = removido.anterior
        self._final.proximo = None
        removido.anterior = None
        self._quantidade -= 1
        return removido.conteudo
    
    def remover(self,posicao):
        if posicao == 0:
            return self.remover_do_inicio()
        if posicao == self.quantidade - 1:
            return self.remover_do_final()
        removido = self._celula(posicao)
        esq = removido.anterior
        dir = removido.proximo
        esq.proximo = dir
        dir.anterior = esq
        removido.anterior = None
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo
    
#a biblioteca padrão de python possui a função "deque" que funciona como uma lista duplamente encadeada
#para usá-la: from collections import deque