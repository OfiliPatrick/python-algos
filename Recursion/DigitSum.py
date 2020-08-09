def digitSum(n):
    if n < 10:
        return n
    
    last_digit = n % 10
    remaining = n // 10
    
    return last_digit + digitSum(remaining)

print(digitSum(43214))