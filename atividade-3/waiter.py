# https://www.beecrowd.com.br/judge/pt/problems/view/2373

n = int(input())

glasses_dropped = 0
for _ in range(n):
    l, c = map(int, input().split())
    
    if l - c > 0:
        glasses_dropped += c

print(glasses_dropped)