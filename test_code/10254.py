for _ in range(int(input())):
    point_list = []
    temp, answer = 0, []
    for _ in range(int(input())):
        point_list.append(list(map(int, input().split(' '))))
    for point in point_list:
        for another_point in point_list:
            compare = (another_point[0] - point[0]) ** 2 + (another_point[1] - point[1]) ** 2
            if compare >= temp:
                temp = compare
                answer = another_point + point
    print(answer[0], answer[1], answer[2], answer[3])
