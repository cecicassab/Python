from listas.lista_ligada import No,ListaLigada
       

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        
    def __repr__(self):
        return "{}\n{}".format(self.nome,self.endereco)
    
    
def main():
    loja1 = Loja("Vilela", "Santa Rita, 504")
    loja2 = Loja("Noa Noa", "PH Rolfs, 432")
    loja3 = Loja("Amantino", "Santa Barbara, 24")
    
    lista = ListaLigada()
    
    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    
    print(lista.quantidade)
    
    lista.inserir(0,loja3)
    lista.imprimir()
    
main()