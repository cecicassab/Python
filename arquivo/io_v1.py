arquivo = open("pessoas.csv")
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print("nome {} idade {}".format(*registro.split(',')))