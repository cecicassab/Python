
try:
    arquivo = open("pessoas.csv")
    for registro in arquivo:
        print("nome {} idade {}".format(*registro.strip().split(',')))
finally:
    arquivo.close()
    
if arquivo.close:
    print("Arquivo fechado com sucesso!")

