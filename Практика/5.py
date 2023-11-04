n = int(input())
while n >= 10:
    total = 0
    while n > 0:
        digit, n = n % 10, n // 10
        total += digit
    n = total
print(n)
