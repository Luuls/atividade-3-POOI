# https://www.beecrowd.com.br/judge/pt/runs/code/32414768

money_values = {100 * 100: 0, 50 * 100: 0, 20 * 100: 0, 10 * 100: 0, 5 * 100: 0, 2 * 100: 0}
coins_values = {1 * 100: 0, 0.50 * 100: 0, 0.25 * 100: 0, 0.10 * 100: 0, 0.05 * 100: 0, 0.01 * 100: 0}

money = float(input()) * 100

print('NOTAS:')
for value in money_values:
    money_values[value] = money // value
    money -= money_values[value] * value
    
    print(f'{money_values[value]:.0f} nota(s) de R$ {value / 100:.2f}')
    
print('MOEDAS:')
for value in coins_values:
    coins_values[value] = money // value
    money -= coins_values[value] * value
    
    print(f'{coins_values[value]:.0f} moeda(s) de R$ {value / 100:.2f}')