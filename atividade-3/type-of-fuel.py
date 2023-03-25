# https://www.beecrowd.com.br/judge/pt/problems/view/1134

from dataclasses import dataclass

@dataclass
class Fuel:
    name: str
    times_used: int = 0

types_of_fuel = [Fuel('Alcool'), Fuel('Gasolina'), Fuel('Diesel')]

possible_values = range(1, 5)
while True:
    fuel_type = int(input())
    while fuel_type not in possible_values:
        fuel_type = int(input())
        
    if fuel_type == 4:
        break
       
    types_of_fuel[fuel_type - 1].times_used += 1
    
print('MUITO OBRIGADO')
for fuel in types_of_fuel:
    print(f'{fuel.name}: {fuel.times_used}')