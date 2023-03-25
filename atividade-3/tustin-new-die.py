# https://www.beecrowd.com.br/judge/pt/problems/view/2600

n = int(input())

for _ in range(n):
    d3 = int(input())
    d1, d2, d6, d5 = map(int, input().split())
    d4 = int(input())

    face_set = set([d1, d2, d3, d4, d5, d6])
    
    if len(face_set) != 6 or 0 in face_set:
        print('NAO')
        continue

    if d3 + d4 == 7 and d1 + d6 == 7 and d2 + d5 == 7:
        print('SIM')

    else:
        print('NAO')
