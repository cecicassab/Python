def sequencia():
    x = 0
    while True:
        x = x+1
        yield x
    
    
if __name__ == '__main__':
    seq = sequencia()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
