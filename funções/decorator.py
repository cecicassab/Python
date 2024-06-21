def log(funciton):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função {funciton.__name__}')
        print(f'args {args}')
        print(f'kwargs {kwargs}')
        resultado = funciton(*args, **kwargs)
        print(f'Resultado da chamada {resultado}')
        return resultado
    return decorator


@log
def soma(x,y):
    return x+y


@log
def sub(x,y):
    return x-y


if __name__ == "__main__":
    soma(4,3)
    sub(9,5)