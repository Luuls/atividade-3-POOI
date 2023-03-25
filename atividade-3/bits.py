# https://www.beecrowd.com.br/judge/pt/problems/view/2187

values = {50: 0, 10: 0, 5: 0, 1: 0}

v = int(input())

test_number = 1
while v != 0:
    money = v
    for value in values:
        values[value] = money // value
        money -= value * values[value]

    print(f'Teste {test_number}')
    a, b, c, d = values.values()
    print(a, b, c, d, sep=' ')
    print('')

    v = int(input())
    test_number += 1
