import math
def allPrimes(n):
    def isPrime(num):
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True

    for num in range(2, n+1):
        if isPrime(num):
            print(num)

print(allPrimes(18))
