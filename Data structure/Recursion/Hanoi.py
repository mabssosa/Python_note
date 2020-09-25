def hanoi(n, a, b, c):
    if n == 1: # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print(a, "->", b)
        return

    # 원반 n - 1개를 c로 이동(b를 보조 기둥으로)
    hanoi(n - 1, a, c, b)
    # 가장 큰 원반을 목적지로 이동
    print(a, "->", b)
    # c에 있는 원반 n-1개를 목적지로 이동(a를 보조 기둥으로)
    hanoi(n - 1, c, b, a)

print("n = 1")
hanoi(1, 1, 3, 2) # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 2")
hanoi(2, 1, 3, 2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 3")
hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)