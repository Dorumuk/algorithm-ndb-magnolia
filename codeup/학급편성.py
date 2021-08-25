# 💩
n, m = input().split()
students = int(n)
max = int(m)
cnt = 0

def loop(first_value):
    rest_value = students - first_value
    count = 0
    for j in range(rest_value - 1):
        if (first_value > count + 1): count +=1
        elif (first_value == count + 1):
            if (rest_value >= first_value * 2):
                count += (loop( rest_value - count) - 1)
        else: break
    return count

for i in range(students):
    first_value = i + 1
    if(first_value <= max):
        cnt += loop(first_value)
print (cnt)

# n, m = input().split()

# students = int(n)
# max = int(m)
# cnt = 0
# for i in range(students):
#     first_value = i + 1
#     if(first_value <= max):
#         rest_value = students - first_value
#         tmp = 1
#         for j in range(rest_value - 1):
#             if (first_value > tmp): tmp +=1
#             else: break
#         cnt += tmp
# print (cnt)

# def loop(first_value):
#     if(first_value <= max):
#         rest_value = students - first_value
#         for j in range(1, rest_value):
#             if (first_value == j):
#                 if (rest_value >= first_value * 2):
#                     loop( rest_value - j)
#             else: break
#         cnt += j