import csv

with open('pessoas.csv') as arquivo:
    for pessoa in csv.reader(arquivo):
        print('Nome: {} Idade: {}'.format(*pessoa))
        

