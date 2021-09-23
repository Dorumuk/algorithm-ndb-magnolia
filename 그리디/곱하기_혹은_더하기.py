# 곱하기 혹은 더하기
# ch11 그리디

s = input()
sum = int(s[0])

for i in range(len(s) -1):
    a = sum + int(s[i + 1])
    b = sum * int(s[i + 1])
    if (a > b):
        sum = a
    else:
        sum = b
print(sum)