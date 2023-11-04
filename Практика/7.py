
d = int(input())
n = int(input())
result = ''
while d != 0:
    digit, d = d % n, d // n
    if digit > 9:
        digit = chr(ord('A') + digit - 10)
    result = str(digit) + result
print(result)
