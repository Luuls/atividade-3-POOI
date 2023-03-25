# https://www.beecrowd.com.br/judge/en/problems/view/2229

i = 1
while (n := int(input())) != -1:
    side_size = 2 ** (n + 1)
    steps_till_mid = side_size // 2

    # soma de PA de 1 a n com razão 1
    pieces = 2 * ((steps_till_mid + 1) * steps_till_mid // 2) + (steps_till_mid + 1) 

    print(f'Teste {i}')
    print(f'{pieces}\n')

    i += 1

