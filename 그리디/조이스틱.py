#Programmers Quiz
# chr(45) == 45
# ord("A") == 65

name = input()
cnt = 0
MAX = 25
nList = []


for i in range(len(name)):
    num = ord(name[i]) - 65
    if(num < 14):
        nList.append(num)
        cnt += num
    else:
        nList.append(MAX - num)
        cnt += num

# for tmp in nList[1:]:
#     if tmp > 0:
