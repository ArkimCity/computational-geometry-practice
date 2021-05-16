x, y = 0, 0
per_area, polygon, answer = int(input()), [[x,y]], 0
while True:
    try:
        direction, length = map(int, input().split(' '))
        if direction == 1:
            x += length
        elif direction == 2:
            x -= length
        elif direction == 3:
            y -= length
        elif direction == 4:
            y += length
        polygon.append([x,y])
    except:
        break

for i in range(len(polygon) - 1):
    answer += ((polygon[i][0] * polygon[i + 1][1]) - (polygon[i + 1][0] * polygon[i][1]))
print(int(abs(answer) * per_area / 2))