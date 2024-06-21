def fibonnaci(sequencia=None):
    sequencia = sequencia or [0,1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    print(fibonnaci())