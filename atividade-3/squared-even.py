# https://www.beecrowd.com.br/judge/pt/problems/view/1073

n = int(input())

for number in range(2, n + 1, 2):
    print(f'{number}^2 = {number ** 2}')
