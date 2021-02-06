def fattoriale(n):
    if n == 1:
        return n
    else:
        result = n * fattoriale(n-1)
        return result