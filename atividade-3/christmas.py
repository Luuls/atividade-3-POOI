# https://www.beecrowd.com.br/judge/pt/problems/view/2139

months_days = [
    31,
    29,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

CHRISTMAS_DAY = 360

while True:
    try:
        month, day = map(int, input().split())

        days = sum(months_days[0:month - 1]) + day

        if days == CHRISTMAS_DAY - 1:
            print('E vespera de natal!')

        elif days == CHRISTMAS_DAY:
            print('E natal!')

        elif days > CHRISTMAS_DAY:
            print('Ja passou!')

        else:
            print(f'Faltam {CHRISTMAS_DAY - days} dias para o natal!')

    except EOFError:
        break
