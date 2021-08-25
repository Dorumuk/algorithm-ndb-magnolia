# 💩
n, m = input().split()
students = int(n)
max = int(m) 
cnt = 0

def loop(first_value, rest_value):
    count = 0
    if first_value > 1:
        for j in range(1, rest_value + 1):
            if (first_value > j): count +=1
            elif (first_value == j):
                if (rest_value >= first_value * 2):
                    count += start(rest_value)
                else:
                    count +=1
            else: break
    else: count += 1
    return count

def start(datas):
    cnt = 0
    for i in range(1, datas): # i : 1 2 3 4 5
        if (i <= max):
            cnt += loop(i, datas - i)
    return cnt

print (start(students))