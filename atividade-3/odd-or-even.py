# https://www.beecrowd.com.br/judge/pt/problems/view/1074

number = int(input())

for i in range(0, number):
    x = int(input())

    if x == 0:
        print('NULL')
        continue

    if x % 2 == 0:
        print('EVEN ', end='')

    else:
        print('ODD ', end='')

    if x > 0:
        print('POSITIVE')

    else:
        print('NEGATIVE')
