def recsum(n):
    if n == 1:
        return 1

    return n + recsum(n - 1)
    
print(recsum(4))

