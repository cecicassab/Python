def fatorial(x):
    if x==0:
        return 1
    else:
        return x * fatorial(x-1)
    
    
print(f'Fatorial de 10 = {fatorial(10)}')
