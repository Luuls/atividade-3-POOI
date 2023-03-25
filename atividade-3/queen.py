# https://www.beecrowd.com.br/judge/pt/problems/view/1087

while True:
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break

    if x2 - x1 == 0 and y2 - y1 == 0:
        print(0)
        continue

    elif x2 - x1 == 0 or y2 - y1 == 0 or abs(x2 - x1) == abs(y2 - y1):
        print(1)
        continue

    else:
        print(2)
        continue
