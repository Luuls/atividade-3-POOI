# https://www.beecrowd.com.br/judge/pt/problems/view/2247

i = 1

while (n := int(input())) != 0: 
    print(f'Teste {i}')

    bank_j, bank_z = 0, 0
    for _ in range(n):
        j, z = map(int, input().split())
        bank_j += j
        bank_z += z
        print(bank_j - bank_z)

    print('')

    i += 1    