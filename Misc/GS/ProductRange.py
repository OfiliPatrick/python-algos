def productRange(x, y, z):
    def compare(n, prod):
        str_n =  set(str(n))
        str_prod = str(prod)
        for number in str_prod:
            if number in str_n:
                return True

        return False

    cnt = 0
    for num in range(y, z + 1):
        product = x * num
        if not compare(num, product):
            cnt += 1     
    return cnt

# print(productRange(2, 10, 12))

# print(productRange(2,5,15))
