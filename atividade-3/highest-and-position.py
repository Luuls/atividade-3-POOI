# https://www.beecrowd.com.br/judge/pt/problems/view/1080

highest = int(input())
index = 1

for i in range(1, 100):
    number = int(input())
    if number > highest:
        highest = number
        index = i + 1


print(highest)
print(index)
