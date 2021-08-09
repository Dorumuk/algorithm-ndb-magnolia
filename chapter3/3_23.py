n = int(input())
list = []

for i in range(n):
    name, kor, eng, math = input().split(' ')
    list.append((name, kor, eng, math))

print(list)