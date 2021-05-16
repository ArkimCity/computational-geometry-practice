x11, y11, x12, y12, x21, y21, x22, y22 = map(int, input().strip().split(' '))
def checker(x11, y11, x12, y12, x21, y21, x22, y22):
    return True if ((x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)) * ((x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)) < 0 else False
if (y12 - y11) * (x22 - x21) == (y22 - y21) * (x12 - x11):
    print(0)
else:
    if checker(x11, y11, x12, y12, x21, y21, x22, y22) and checker(x21, y21, x22, y22, x11, y11, x12, y12):
        print(1)
    else:
        print(0)
