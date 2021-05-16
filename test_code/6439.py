def is_diving(x11, y11, x12, y12, x21, y21, x22, y22):
    return True if ((x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)) * ((x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)) <= 0 else False
def checker(x11, y11, x12, y12, x21, y21, x22, y22):
    if (y12 - y11) * (x22 - x21) - (y22 - y21) * (x12 - x11) == 0:
        return False if min(x11, x12) > max(x21, x22) or max(x11, x12) < min(x21, x22) or min(y11, y12) > max(y21, y22) or max(y11, y12) < min(y21, y22) else True
    else:
        return True if is_diving(x11, y11, x12, y12, x21, y21, x22, y22) and is_diving(x21, y21, x22, y22, x11, y11, x12, y12) else False
for _ in range(int(input())):
    xs, ys, xe, ye, x1, y1, x2, y2 = map(int, input().split(' '))
    if ((min(x1, x2) <= xs and xs <= max(x1, x2) and min(y1, y2) <= ys and ys <= max(y1, y2)) or 
        (min(x1, x2) <= xe and xe <= max(x1, x2) and min(y1, y2) <= ye and ye <= max(y1, y2))):
        print('T')
    else:
        if (checker(xs, ys, xe, ye, x1, y1, x1, y2) or checker(xs, ys, xe, ye, x1, y1, x2, y1)
            or checker(xs, ys, xe, ye, x1, y2, x2, y2) or checker(xs, ys, xe, ye, x2, y1, x2, y2)):
            print('T')
        else:
            print('F')