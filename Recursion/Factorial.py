#Iterative Approach
def fact(n):
    if n == 0 or n ==1:
        return 1
    res =1
    while n != 1:
        res*=n
        n= n-1
    return res

print(fact(1))



# Recursive approach

def rec_fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)
    
print(rec_fact(5))


