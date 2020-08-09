def digit_sum(n):
    result = 0

    while n != 0:
        last_digit = n % 10
        result += last_digit
        n = n // 10

    return result

print(digit_sum(43219))