from datetime import datetime, timedelta


class Projeto:
    def __init__(self,nome):
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
        return self.tarefas.__iter__()
        
    def add(self,descricao,vencimento=None):
        self.tarefas.append(Tarefa(descricao,vencimento))
        
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self,descricao):
        return [tarefa for tarefa in self.tarefas 
                if tarefa.descricao == descricao][0]
        
    def __str__(self) -> str:
        return f'{self.nome} ({len(self.pendentes())}) tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento
        
    def concluir(self):
        self.feito = True
        
    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        return f'{self.descricao} ' + ' '.join(status)
    
    
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao,vencimento)
        self.dias = dias
    
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao,novo_vencimento,self.dias)
    
    
def main():
    casa = Projeto('Tarefas da Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa.add('Varrer a cozinha', datetime.now() + timedelta(days=3,minutes=12))
    casa.tarefas.append(TarefaRecorrente('Trocar lençois', datetime.now(),7))
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
            
    