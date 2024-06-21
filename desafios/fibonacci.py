def fibonacci(n, sequencia=(0,1)):
    if len(sequencia) == n:
        return sequencia
    return fibonacci(n, sequencia + (sum(sequencia[-2:]),))


for i in fibonacci(10):
    print(i)