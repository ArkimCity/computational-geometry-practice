from math import factorial
for _ in range(int(input())):
    n, m = map(int, input().split(' '))
    ans = 1
    for i in range(min(m - n, n)):
        ans *= (m - i)
        ans /= (i + 1)
    print(round(ans))
    