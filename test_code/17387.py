x11, y11, x12, y12 = map(int, input().split(' '))
x21, y21, x22, y22 = map(int, input().split(' '))
def checker(x11, y11, x12, y12, x21, y21, x22, y22):
    answer = False
    if ((x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)) * ((x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)) <= 0:
        answer = True
    return answer
if (y12 - y11) * (x22 - x21) - (y22 - y21) * (x12 - x11) == 0:
    if min(x11, x12) > max(x21, x22) or max(x11, x12) < min(x21, x22) or min(y11, y12) > max(y21, y22) or max(y11, y12) < min(y21, y22):
        print(0)
    else:
        print(1)
else:
    if checker(x11, y11, x12, y12, x21, y21, x22, y22) and checker(x21, y21, x22, y22, x11, y11, x12, y12):
        print(1)
    else:
        print(0)
