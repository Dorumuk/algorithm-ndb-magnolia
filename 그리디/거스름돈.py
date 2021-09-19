n = int(input())
m = [500, 100, 50, 10]
cnt = 0

for mi in m:
    cnt += n // mi
    n = int(n % mi) # n %= mi

print(cnt)
