from prac_08.unreliable_car import UnreliableCar

count = 0
car = UnreliableCar('a', 120, 1)
while car.fuel > 0:
    count += 1
    car.drive(30)
    print(car)
print(count)
