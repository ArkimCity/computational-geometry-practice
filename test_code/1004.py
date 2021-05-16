for _ in range(int(input())):
    answer = 0
    sx, sy, ex, ey = map(int, input().split(' '))
    for _ in range(int(input())):
        cx, cy, cr = (map(int, input().split(' ')))
        t1 = (cx - sx) ** 2 + (cy - sy) ** 2 < cr ** 2
        t2 = (cx - ex) ** 2 + (cy - ey) ** 2 < cr ** 2
        if (t1 or t2) and (not (t1 and t2)) :
            answer += 1
    print(answer)
# 한쪽을 원이 포함하면 카운트. 근데 둘다 포함하면 제외