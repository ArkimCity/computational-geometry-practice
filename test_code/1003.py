for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        a, b = 1, 0
        for i in range(n - 1):
            a, b = a + b, a
        print(b, a)