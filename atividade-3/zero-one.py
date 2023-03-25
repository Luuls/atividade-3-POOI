# https://www.beecrowd.com.br/judge/pt/problems/view/1467

while True:
    try:
        a, b, c = map(int, input().split())

        if a == b and b == c:
            print('*')

        elif a == b and a != c:
            print('C')

        elif a == c and a != b:
            print('B')

        elif b == c and b != a:
            print('A')

    except EOFError:
        break
