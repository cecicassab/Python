from datetime import datetime


class Projeto:
    def __init__(self,nome):
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
        return self.tarefas.__iter__()
        
    def add(self,descricao):
        self.tarefas.append(Tarefa(descricao))
        
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self,descricao):
        return [tarefa for tarefa in self.tarefas 
                if tarefa.descricao == descricao][0]
        
    def __str__(self) -> str:
        return f'{self.nome} ({len(self.pendentes())}) tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        
    def concluir(self):
        self.feito = True
        
    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')
    
    
def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    casa.add('Varrer a cozinha')
    print(casa)
    
    casa.procurar('Lavar prato').concluir()   
    for tarefa in casa:
        print(f' - {tarefa}')       
        
    mercado = Projeto('Mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Ovos')
    print(mercado)

if __name__ == '__main__':
    main()
            
    