# 두 원 사이의 관계 로 가능한 경우의 수
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    d_squared = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if x1==x2 and y1==y2 and r1==r2: #일치
        print(-1)
    elif d_squared == (r1 + r2) ** 2: #외접
        print(1)
    elif d_squared == (r1 - r2) ** 2: # 내접
        print(1)
    elif d_squared > (r1 + r2) ** 2: #분리
        print(0)
    elif d_squared ** 0.5 + min(r1, r2) < max(r1, r2): #완전포함
        print(0)
    else:
        print(2)