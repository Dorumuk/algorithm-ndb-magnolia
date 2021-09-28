# 큰 수 만들기
#Programmers
# 얕은 복사([:]) 깊은 복사(copy.deepcopy(a))

# index() 함수는 리스트에서 원하는 값의 인덱스를 불러온다. 중복되는 수가 있을 경우 가장 앞(왼)쪽에 있는 수의 인덱스를 반환한다.

number = input()
k = int(input())
numList = [ number[i] for i in range(len(number))] # 넘버 리스트
result_len = len(number) - k
max_v_idx = len(number) # 기준이 되는 가장 큰 수
cnt = 0

tmp_list = numList[:] # 얕은 복사 # 문제(3)
while(len(number[max_v_idx:]) < result_len): # 문제(1)
    # tmp_list[max_v_idx] = 0
    if (max_v_idx != len(number)): tmp_list.pop(max_v_idx)
    max_v_idx = tmp_list.index(max(tmp_list))

new_list = numList[max_v_idx:]
for j in range(1,len(new_list) - 1):
    if(new_list[j] < new_list[j + 1]):
        new_list.pop(j)
        cnt+=1
    if(cnt == k - max_v_idx): break

print("".join(new_list))

# 채점 결과
# 정확성: 8.3
# 합계: 8.3 / 100.0