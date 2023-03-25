# https://www.beecrowd.com.br/judge/pt/problems/view/1221

n = int(input())

for _ in range(0, n):
    x = int(input())

    is_prime = True
    i = 2
    while i*i < x:
        if x % i == 0:
            is_prime = False
            break

        i += 1

    if is_prime:
        print('Prime')

    else:
        print('Not Prime')
