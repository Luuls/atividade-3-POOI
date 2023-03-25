# https://www.beecrowd.com.br/judge/pt/problems/view/1323

n = int(input())

while n != 0:
    number_of_squares = 0
    for i in range(1, n + 1):
        number_of_squares += i ** 2

    print(number_of_squares)

    n = int(input())
