burger_m = []
drink_m = []
for i in range(3):
    burger = int(input())
    burger_m.append(burger)
for i in range(2):
    drink = int(input())
    drink_m.append(drink)
print(min(burger_m)+min(drink_m)-50)