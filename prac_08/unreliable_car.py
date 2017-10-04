from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name='', fuel=0, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.random() * 100
        if random_number < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            return 0
