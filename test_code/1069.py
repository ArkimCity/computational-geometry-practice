x, y, d, t = map(int, input().split(' '))
distance = (x ** 2 + y ** 2) ** 0.5

if d > t:
    base_time = (distance // d) * t
    a1 = distance - (distance // d) * d
    a2 = t + abs(d - a1)
    a3 = t * 2
    if distance <= 2 * d:
        print(min(base_time + min(a1, a2, a3), 2 * t))
    else:
        print(base_time + min(a1, a2, a3))

else:
    print(min(distance, t * 2, t + abs(distance - d)))
