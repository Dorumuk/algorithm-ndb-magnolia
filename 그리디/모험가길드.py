# ch11 그리디

n = input()
group = list(map(int, input().split()))
cnt = 0
rest = 0

# 내림차순으로 미리 정렬을 한다.
group.sort(reverse=True)

for man in group:
    if (rest == 0):
        cnt+=1
        rest = man - 1 # 자신을 제외한 나머지 공간의 수를 계산
    else:
        rest-=1

print(cnt)