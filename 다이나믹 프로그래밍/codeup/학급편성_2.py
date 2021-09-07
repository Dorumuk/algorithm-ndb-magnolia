# https://www.codeup.kr/problem.php?id=4045
# 08/25/2021
# ✨성공
n, m = input().split()
students = int(n)
max = int(m) 

cnt = 0
def getCount(students, prev_F):
    count = 0
    for first in range(1, students + 1): # 1 ~ 8
        if first <= max:
            if first == 1:
                count += 1
            else:
                if(students - first > 0):
                    count += getCount(students - first, first)
                else:
                    count += 1
            if first == prev_F: break
    return count


print(getCount(students, -1))