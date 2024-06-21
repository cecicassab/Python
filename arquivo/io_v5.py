
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print("nome {} idade {}".format(*pessoa), file=saida)
        
if arquivo.close:
    print("Arquivo fechado com sucesso!")

