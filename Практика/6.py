n = int(input())
counter = 0
for n in range(1, n + 1):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print(n, end=' ')
        counter += 1
if counter == 0:
    print(None)
