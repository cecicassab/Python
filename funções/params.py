def params(*args, **kwargs):
    print(f'args {args} kwargs {kwargs}')
    
    
params(1,2,3,4)
params(1,2,3,numero=7,nome='Joao')