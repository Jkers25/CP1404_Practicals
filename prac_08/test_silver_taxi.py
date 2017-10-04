from prac_08.silver_taxi import SilverTaxi

car = SilverTaxi('a', 300, 2)
car.drive(18)
print(car)
print('${:.2f}'.format(car.get_fare()))
