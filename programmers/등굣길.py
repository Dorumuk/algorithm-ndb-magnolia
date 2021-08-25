import math
#→,↓ 최단거리 문제
# https://programmers.co.kr/learn/courses/30/lessons/42898
# 08/25/2021
# ✨성공

def goto(p_m, p_n):
    return math.factorial(p_m + p_n) / (math.factorial(p_m) * math.factorial(p_n))

def solution(m, n, puddles):
    answer = 0
    no_ways = 0
    gm, gn = m -1, n -1
    all_ways = goto(gm + gn)
    
    for puddle in puddles:
        pm, pn = puddle[0] - 1 , puddle[1] - 1
        npm, npn = gm - pm, gn - pn
        no_ways += goto(pm + pn) * goto(npm + npn)
        
    answer = (all_ways - no_ways ) % 1000000007
    
    return answer

m, n, puddles = input().split()
print(solution(m, n, puddles))