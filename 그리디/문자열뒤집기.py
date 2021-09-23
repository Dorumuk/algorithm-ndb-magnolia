s = input()
cnt = 0
betw = 1 # between : 사이에 있는 수

for i in range(len(s) -1):
    if s[i] != s[i + 1]:
        if betw == 1:
            cnt +=1
            betw = 0
        else:
            betw = 1

print(cnt)