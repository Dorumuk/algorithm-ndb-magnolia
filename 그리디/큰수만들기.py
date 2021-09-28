# 큰 수 만들기
#Programmers
# 얕은 복사([:]) 깊은 복사(copy.deepcopy(a))

# index() 함수는 리스트에서 원하는 값의 인덱스를 불러온다. 중복되는 수가 있을 경우 가장 앞(왼)쪽에 있는 수의 인덱스를 반환한다.

number = input()
k = int(input())
numList = [ number[i] for i in range(len(number))] # 넘버 리스트
result_len = len(number) - k
max_v_idx = len(number) # 기준이 되는 가장 큰 수

tmp_list = numList[:] # 얕은 복사 # 문제(3)
while(len(number[max_v_idx:]) < result_len): # 문제(1)
    # tmp_list[max_v_idx] = 0
    if (max_v_idx != len(number)): tmp_list.pop(max_v_idx)
    max_v_idx = tmp_list.index(max(tmp_list))
    

for i in range(k): # 제거할 수 있는 수 반복
    if(max_v_idx > 0):
        numList.pop(max_v_idx - 1)
        max_v_idx -= 1 # 문제(2)
    else:
        # 문제(4)
        for j in range(len(numList)):
            if( numList[j] < numList[j + 1]):
                numList.pop(j)
                break

print("".join(numList))

# 채점 결과
# 정확성: 75.0 (시간초과 3문제)
# 합계: 75.0 / 100.0