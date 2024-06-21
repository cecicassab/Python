import sys


def converte_conceito(nota):
    if nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    else:
        return 'E-'
    
def help(nota):
    if nota > 10 or nota < 0:
        print("Nota inválida")
        print("Valor digitado deve estar entre 0 e 10")
        sys.exit(1)
        
    #elif not nota.isnumeric:
     #   print("O argumento deve ser um valor numérico")
    
    
nota = float(input("Digite a nota do aluno: "))
help(nota)
print("Nota: " + converte_conceito(nota))