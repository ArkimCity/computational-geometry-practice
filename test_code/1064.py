# 이 세개의 점으로 만들어지는 삼각형의 세 변을 한번씩 다른 점을 체크
# 이는 다른 두 점의 중점으로 대칭 이동 시키면 된다.
# 여기 세개의 점이 서로 모두 평행하다면 -1이 된다.

xA, yA, xB, yB, xC, yC = map(int, input().split(' '))
point_list = [[xA,yA], [xB,yB], [xC,yC]]
(yA- yB) != 0 and (yB - yC) != 0
if (xA - xB) * (yB - yC) == (xB - xC) * (yA - yB):
    print(-1)
else:
    len_lst = []
    for i in range(len(point_list)):
        others = [point_list[i - 1], point_list[i - 2]]
        new_x = others[0][0] + others[1][0] - point_list[i][0]
        new_y = others[0][1] + others[1][1] - point_list[i][1]
        len_one = ((new_x - point_list[i - 1][0]) ** 2 + (new_y - point_list[i - 1][1]) ** 2) ** 0.5
        len_two = ((point_list[i - 1][0] - point_list[i][0]) ** 2 + (point_list[i - 1][1] - point_list[i][1]) ** 2) ** 0.5
        len_lst.append((len_one + len_two) * 2)
    print(max(len_lst) - min(len_lst))
    #A 를 BC 중점에 에 대칭
