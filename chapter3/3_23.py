n = int(input())
list = []
'''
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''

for i in range(n):
    name, kor, eng, math = input().split(' ')
    list.append([name, kor, eng, math])

def selection_sort(arr, type, vector, excpt_list, bpList):
    bpList = []
    for i in range(len(arr)): # -1
        min_idx = i

        for j in range(i + 1, len(arr)):
            if (arr[j][type] * vector > arr[min_idx][type]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        if (arr[i -1][type]):
            if (arr[i - 1][type] == arr[i][type]):
                excpt_list[i] = 1
            else:
                excpt_list[i] = 0
                bpList = i

    print (excpt_list)
    return arr, excpt_list

def start ():
    excpt_list = [0 for i in range(n)]
    result, excpt_list = selection_sort(list, 1, 1, excpt_list) # kor
    print(result)
    # print(excpt_list)

start()