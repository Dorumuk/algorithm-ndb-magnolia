def main():
    g = int(input()) # 탑승구 수
    p = int(input()) # 비행기 수
    gate_list = [0 for _ in range(g + 1)]
    get_out = False
    count = 0

    for i in range(1, p + 1):
        if get_out: break
        available_gates = int(input())
        for j in reversed(range(1, available_gates + 1)): # 4 3 2 1
            if (gate_list[j] == 0):
                gate_list[j] = i
                count+=1
                break
            else:
                if (j == 1):
                    get_out = True
                    break

    print(count)

main()