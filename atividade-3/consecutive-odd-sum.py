# https://www.beecrowd.com.br/judge/pt/problems/view/1099

n = int(input())

for _ in range(0, n):
    x, y = map(int, input().split())

    sum = 0

    if x > y:
        aux = y
        y = x
        x = aux

    for number in range(x + 1, y):
        if number % 2 != 0:
            sum += number

    print(sum)
